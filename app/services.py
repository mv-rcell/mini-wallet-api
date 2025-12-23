from datetime import datetime
from typing import List
from fastapi import HTTPException
from .models import Transaction, TransactionCreate, TransactionType

transactions: List[Transaction] = []
current_balance: float = 0.0
transaction_id_counter = 1


def add_transaction(data: TransactionCreate) -> Transaction:
    global current_balance, transaction_id_counter

    if data.type == TransactionType.debit and data.amount > current_balance:
        raise HTTPException(
            status_code=400,
            detail="Insufficient balance for debit transaction"
        )

    if data.type == TransactionType.credit:
        current_balance += data.amount
    else:
        current_balance -= data.amount

    transaction = Transaction(
        id=transaction_id_counter,
        amount=data.amount,
        type=data.type,
        created_at=datetime.utcnow()
    )

    transaction_id_counter += 1
    transactions.append(transaction)
    return transaction


def get_transactions() -> List[Transaction]:
    return transactions


def get_balance() -> float:
    return current_balance
