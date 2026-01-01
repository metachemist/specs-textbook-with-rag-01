from typing import List, Dict, Any
from ..core.qdrant import qdrant_client
from qdrant_client.http import models
from fastembed import TextEmbedding
import logging

logger = logging.getLogger(__name__)


def search_context(query: str, top_k: int = 3) -> str:
    """
    Search for relevant context in the Qdrant vector database
    """
    try:
        # Get the embedding for the query using FastEmbed
        embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        query_embedding = list(embedding_model.embed([query]))[0].tolist()
        
        # Search in Qdrant for similar vectors
        search_results = qdrant_client.search(
            collection_name="textbook_content",  # This should match the collection name in your ingestion script
            query_vector=query_embedding,
            limit=top_k,
            with_payload=True
        )
        
        # Extract the context from the search results
        context_parts = []
        sources = []
        
        for result in search_results:
            if result.payload:
                content = result.payload.get("content", "")
                source = result.payload.get("source", "Unknown source")
                
                context_parts.append(content)
                sources.append(source)
        
        # Combine the context parts
        full_context = "\n\n".join(context_parts)
        
        logger.info(f"Found {len(context_parts)} relevant context chunks for query: {query[:50]}...")
        
        return full_context
    except Exception as e:
        logger.error(f"Error searching context: {e}")
        raise