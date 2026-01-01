from fastapi import APIRouter, HTTPException
from typing import List
from ..models.schemas import ChatQueryRequest, ChatQueryResponse
from ..services.rag_service import search_context
from ..services.openrouter_service import generate_answer

router = APIRouter()


@router.post("/", response_model=ChatQueryResponse)
async def chat_endpoint(request: ChatQueryRequest):
    """
    Main chat endpoint that processes user queries using RAG
    """
    try:
        # Search for relevant context using the RAG service
        context = search_context(request.query)
        
        if not context:
            # If no context is found, we can still try to answer based on the model's knowledge
            context = "No specific context found in the textbook. Please answer based on general knowledge."
        
        # Generate an answer using the OpenRouter service
        answer = await generate_answer(context, request.query)
        
        # For now, we'll return a simple response with the answer
        # In a real implementation, you'd want to extract the actual sources
        sources = ["textbook_content"]  # Placeholder - would be actual sources in real implementation
        
        return ChatQueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")