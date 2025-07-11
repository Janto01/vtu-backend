from fastapi import APIRouter, Request
import httpx
import os
import uuid

router = APIRouter(prefix="/betting", tags=["Betting"])

VTU_API_KEY = os.getenv("VTU_API_KEY")
VTU_USER_ID = os.getenv("VTU_USER_ID")
BASE_CALLBACK = os.getenv("BASE_URL")

@router.post("/")
async def fund_betting(request: Request):
    data = await request.json()
    company = data["company"]
    customer_id = data["customer_id"]
    amount = data["amount"]
    request_id = str(uuid.uuid4())

    url = "https://www.nellobytesystems.com/APIBettingV1.asp"
    params = {
        "UserID": VTU_USER_ID,
        "APIKey": VTU_API_KEY,
        "BettingCompany": company,
        "CustomerID": customer_id,
        "Amount": amount,
        "RequestID": request_id,
        "CallBackURL": f"{BASE_CALLBACK}/betting/callback"
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()
