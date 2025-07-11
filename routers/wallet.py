from fastapi import APIRouter, Request
from typing import Dict
import os

router = APIRouter(prefix="/wallet", tags=["Wallet"])

wallets: Dict[str, float] = {}
ADMIN_ID = os.getenv("ADMIN_ID")

@router.get("/balance/{user_id}")
def get_balance(user_id: str):
    return {"user_id": user_id, "balance": wallets.get(user_id, 0.0)}

@router.post("/fund")
async def fund_wallet(request: Request):
    data = await request.json()
    user_id = str(data["user_id"])
    amount = float(data["amount"])
    wallets[user_id] = wallets.get(user_id, 0.0) + amount
    return {"status": "success", "message": f"₦{amount} credited", "balance": wallets[user_id]}

@router.post("/debit")
async def debit_wallet(request: Request):
    data = await request.json()
    user_id = str(data["user_id"])
    amount = float(data["amount"])
    current_balance = wallets.get(user_id, 0.0)
    if current_balance < amount:
        return {"status": "failed", "message": "Insufficient balance"}
    wallets[user_id] -= amount
    return {"status": "success", "message": f"₦{amount} debited", "balance": wallets[user_id]}
