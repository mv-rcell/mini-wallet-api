from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Mini Wallet API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Mini Wallet API is running"}
