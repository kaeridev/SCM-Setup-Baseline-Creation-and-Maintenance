from pydantic import BaseModel, Field
from dataclasses import dataclass
from decimal import Decimal

class Student(BaseModel):
    name: str = Field(..., description="Student's name")
    score: int = Field(..., description="Student's score", ge=0, le=100)


students = [
    Student(name="Alice", score=85),
    Student(name="Bob", score=90),
    Student(name="Charlie", score=78),
    Student(name="James", score=67)
]



@dataclass
class InventoryItem:
    """Represent an inventory item and its unit price."""

    item_name: str
    quantity: int
    price: Decimal


inventory: list[InventoryItem] = [
    InventoryItem("Notebook", 25, Decimal("2.99")),
    InventoryItem("Pen", 100, Decimal("0.99")),
    InventoryItem("Backpack", 12, Decimal("24.99")),
]