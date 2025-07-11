from fastapi import APIRouter, Request
import httpx
import os
import uuid

router = APIRouter(prefix="/data", tags=["Data VTU"])

VTU_API_KEY = os.getenv("VTU_API_KEY")
VTU_USER_ID = os.getenv("VTU_USER_ID")
BASE_CALLBACK = os.getenv("BASE_URL")

@router.post("/")
async def buy_data(request: Request):
    data = await request.json()
    number = data["number"]
    plan = data["plan"]  # This is the plan ID, like 1000.0 for 1GB
    network = data["network"]  # '01' for MTN, '02' for GLO, etc.
    request_id = str(uuid.uuid4())

    url = "https://www.nellobytesystems.com/APIDatabundleV1.asp"
    params = {
        "UserID": VTU_USER_ID,
        "APIKey": VTU_API_KEY,
        "MobileNetwork": network,
        "DataPlan": plan,
        "MobileNumber": number,
        "RequestID": request_id,
        "CallBackURL": f"{BASE_CALLBACK}/data/callback"
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()
