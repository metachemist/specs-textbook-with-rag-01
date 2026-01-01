import os
import httpx
from typing import Dict, Any
from ..core.config import settings


async def generate_answer(context: str, query: str) -> str:
    """
    Generate an answer using OpenRouter API with the xiaomi/mimo-v2-flash:free model
    """
    if not settings.OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not set in environment variables")
    
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Prepare the messages for the API
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant for a Physical AI & Humanoid Robotics textbook. Answer questions based on the provided context."
        },
        {
            "role": "user",
            "content": f"Context: {context}\n\nQuestion: {query}\n\nPlease provide a concise answer based on the context, citing specific modules if possible."
        }
    ]
    
    data = {
        "model": "xiaomi/mimo-v2-flash:free",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30.0
        )
        
        if response.status_code != 200:
            raise Exception(f"OpenRouter API request failed with status {response.status_code}: {response.text}")
        
        result = response.json()
        
        # Extract the answer from the response
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Unexpected response format from OpenRouter: {result}")