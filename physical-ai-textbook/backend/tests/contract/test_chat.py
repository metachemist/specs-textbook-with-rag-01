import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_chat_endpoint_structure():
    """
    Test that the chat endpoint returns the expected structure
    """
    client = TestClient(app)

    # This test should fail initially since the endpoint doesn't exist yet
    response = client.post(
        "/api/chat",
        json={"query": "What is ROS 2?", "selected_text": None}
    )

    # We expect a 200 OK response with the expected structure
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"], str)
    assert "sources" in response.json()
    assert isinstance(response.json()["sources"], list)