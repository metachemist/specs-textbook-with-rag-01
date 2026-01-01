from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, DateTime


class TextbookContent(SQLModel, table=True):
    __tablename__ = "textbook_content"

    id: str = Field(default=None, primary_key=True)
    content: str = Field(nullable=False)
    page_url: str = Field(nullable=False)  # URL path to the page containing this content (e.g., "/module-1/ros2")
    chapter: str = Field(nullable=False)  # The chapter/module this content belongs to (e.g., "Module 1")
    created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )