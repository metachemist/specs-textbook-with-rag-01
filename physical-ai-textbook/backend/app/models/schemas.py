from pydantic import BaseModel
from typing import List, Optional


class ChatQueryRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None


class ChatQueryResponse(BaseModel):
    answer: str
    sources: List[str]