from sqlmodel import SQLModel, Field
from typing import Optional
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime


def generate_uuid():
    return str(uuid.uuid4())


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(default_factory=generate_uuid, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    hardware_profile: str = Field(nullable=True)  # User's hardware background (e.g., "Jetson Kit", "Cloud Only")
    coding_level: str = Field(nullable=True)  # User's coding level (e.g., "Python", "C++", "Beginner")
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )