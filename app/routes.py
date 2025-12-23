from fastapi import APIRouter
from .models import TransactionCreate, Transaction
from .services import add_transaction, get_transactions, get_balance
from typing import List

router = APIRouter()


@router.post("/transactions", response_model=Transaction, status_code=201)
def create_transaction(transaction: TransactionCreate):
    return add_transaction(transaction)


@router.get("/transactions", response_model=List[Transaction])
def list_transactions():
    return get_transactions()


@router.get("/balance")
def wallet_balance():
    return {"balance": get_balance()}
