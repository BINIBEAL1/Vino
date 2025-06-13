# This file will hold your database models (tables) and Pydantic schemas (data validation).
# Example placeholder:

from pydantic import BaseModel

class User(BaseModel):
    id: int
    telegram_id: int
    phone: str
    name: str
    balance: float
    # Add more fields as needed
