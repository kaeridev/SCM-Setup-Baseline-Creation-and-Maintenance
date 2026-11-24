"""Students data module."""
from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., description="Student's name")
    score: int = Field(..., description="Student's score", ge=0, le=100)


students = [
    Student(name="Alice", score=85),
    Student(name="Bob", score=90),
    Student(name="Charlie", score=78),
    Student(name="James", score=67)
]