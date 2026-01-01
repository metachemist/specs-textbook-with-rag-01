import os
import glob
from pathlib import Path
from typing import List, Dict, Any
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_docs_directory(docs_path: str) -> List[Dict[str, Any]]:
    """
    Recursively read all .mdx files in the docs directory
    """
    mdx_files = glob.glob(os.path.join(docs_path, "**", "*.mdx"), recursive=True)
    documents = []
    
    for file_path in mdx_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Create document entry
                doc = {
                    "content": content,
                    "source": file_path,
                    "file_name": os.path.basename(file_path)
                }
                documents.append(doc)
                
                logger.info(f"Read file: {file_path}")
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
    
    return documents


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks
    """
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        
        # If this is the last chunk, include the rest
        if end >= len(text):
            chunk = text[start:]
        else:
            # Try to break at sentence boundary
            chunk = text[start:end]
            
            # Find the last sentence boundary within the chunk
            last_period = chunk.rfind('.')
            if last_period > chunk_size // 2:  # Only break if period is reasonably far in
                chunk = text[start:start + last_period + 1]
                end = start + last_period + 1
        
        chunks.append(chunk.strip())
        start = end - overlap if end < len(text) else len(text)
    
    return [chunk for chunk in chunks if chunk.strip()]


def upsert_to_qdrant(documents: List[Dict[str, Any]], collection_name: str = "textbook_content"):
    """
    Upsert documents to Qdrant using FastEmbed for vectorization
    """
    # Initialize Qdrant client
    client = QdrantClient(
        url=os.getenv("QDRANT_URL", "http://localhost:6333"),
        api_key=os.getenv("QDRANT_API_KEY"),
        prefer_grpc=False
    )
    
    # Initialize embedding model
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    # Prepare points for upsert
    points = []
    
    for idx, doc in enumerate(documents):
        content = doc["content"]
        source = doc["source"]
        
        # Chunk the content
        chunks = chunk_text(content)
        
        for chunk_idx, chunk in enumerate(chunks):
            # Generate embedding for the chunk
            embeddings = list(embedding_model.embed([chunk]))
            vector = embeddings[0].tolist()  # Convert to list for Qdrant
            
            # Create a point for Qdrant
            point = models.PointStruct(
                id=idx * 1000 + chunk_idx,  # Create unique ID
                vector=vector,
                payload={
                    "content": chunk,
                    "source": source,
                    "chunk_index": chunk_idx
                }
            )
            points.append(point)
    
    # Create collection if it doesn't exist
    try:
        client.get_collection(collection_name)
        logger.info(f"Collection '{collection_name}' already exists")
    except:
        logger.info(f"Creating collection '{collection_name}'")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),  # Size for BGE-small model
        )
    
    # Upsert the points to Qdrant
    logger.info(f"Upserting {len(points)} points to Qdrant...")
    client.upsert(
        collection_name=collection_name,
        points=points
    )
    
    logger.info(f"Successfully upserted {len(points)} points to Qdrant collection '{collection_name}'")


def main():
    """
    Main function to run the ingestion pipeline
    """
    # Path to the docs directory (relative to the frontend)
    docs_path = os.path.join("..", "frontend", "docs")
    
    if not os.path.exists(docs_path):
        logger.error(f"Docs directory does not exist: {docs_path}")
        return
    
    logger.info(f"Reading documents from: {docs_path}")
    
    # Read all documents
    documents = read_docs_directory(docs_path)
    logger.info(f"Found {len(documents)} documents")
    
    # Upsert to Qdrant
    upsert_to_qdrant(documents)
    
    logger.info("Ingestion pipeline completed successfully!")


if __name__ == "__main__":
    main()