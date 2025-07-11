from fastapi import APIRouter, Request
import os

router = APIRouter(prefix="/webhook", tags=["Paystack Webhook"])

wallets = {}

@router.post("/paystack")
async def paystack_webhook(request: Request):
    body = await request.json()
    event = body.get("event")

    if event == "charge.success":
        data = body.get("data", {})
        metadata = data.get("metadata", {})
        user_id = str(metadata.get("user_id"))
        amount = int(data.get("amount", 0)) / 100

        if user_id:
            wallets[user_id] = wallets.get(user_id, 0.0) + amount
            return {"status": "success", "message": f"₦{amount} credited to {user_id}"}

    return {"status": "ignored"}
