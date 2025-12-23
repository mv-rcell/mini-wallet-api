from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class TransactionType(str, Enum):
    credit = "credit"
    debit = "debit"


class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: TransactionType


class Transaction(TransactionCreate):
    id: int
    created_at: datetime
