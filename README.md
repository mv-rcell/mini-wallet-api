# Mini Wallet API

## Description
A simple FastAPI backend service that manages wallet transactions using in-memory storage.

## Features
- Add credit and debit transactions
- Prevent overdrafts
- View transaction history
- Get current wallet balance

## Tech Stack
- Python
- FastAPI
- Pydantic

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
