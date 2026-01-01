from qdrant_client import QdrantClient
from qdrant_client.http import models
from .config import settings
from fastembed import TextEmbedding


def get_qdrant_client():
    """
    Initialize and return a Qdrant client
    """
    if settings.QDRANT_API_KEY:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=False  # Using REST API instead of gRPC
        )
    else:
        # For local development without API key
        client = QdrantClient(url=settings.QDRANT_URL)
    
    return client


def get_embedding_model():
    """
    Initialize and return a FastEmbed model for local embeddings
    """
    # Using a lightweight model for local embeddings
    model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return model


# Initialize the client and model
qdrant_client = get_qdrant_client()
embedding_model = get_embedding_model()


def initialize_qdrant_collection(collection_name: str, vector_size: int = 384):
    """
    Initialize a Qdrant collection with the specified name and vector size
    """
    try:
        # Check if collection already exists
        qdrant_client.get_collection(collection_name)
        print(f"Collection '{collection_name}' already exists")
    except:
        # Create a new collection if it doesn't exist
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        )
        print(f"Created collection '{collection_name}'")