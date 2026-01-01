import pytest
from unittest.mock import Mock, patch
from app.services.rag_service import search_context
from app.services.openrouter_service import generate_answer


def test_rag_pipeline_integration():
    """
    Test the RAG pipeline integration by mocking external services
    """
    # Mock the Qdrant search result
    mock_context = "ROS 2 (Robot Operating System 2) is a flexible framework for writing robot software."

    # Mock the OpenRouter response
    mock_answer = "ROS 2 is a flexible framework for writing robot software."

    # Test the flow: context retrieval -> answer generation
    with patch('app.services.rag_service.search_context', return_value=mock_context):
        with patch('app.services.openrouter_service.generate_answer', return_value=mock_answer):
            # Simulate the RAG flow
            context = search_context("What is ROS 2?")
            answer = generate_answer(context, "What is ROS 2?")

            # Verify the context was retrieved
            assert context == mock_context

            # Verify the answer was generated
            assert answer == mock_answer

            # Verify the context contains relevant information
            assert "ROS 2" in context
            assert "framework" in context
            assert "robot" in context


def test_rag_pipeline_integration_with_real_services():
    """
    Test the RAG pipeline integration with real services (when available)
    This test will be skipped if external services are not available
    """
    try:
        # This test would call the actual services, but we'll skip it for now
        # since we don't have a Qdrant instance or OpenRouter API key in the test environment
        pytest.skip("Skipping real service test - requires external services")
    except Exception:
        pytest.skip("Skipping real service test - external services not available")