from fastapi import APIRouter, Request
import httpx
import os
import uuid

router = APIRouter(prefix="/electricity", tags=["Electricity"])

VTU_API_KEY = os.getenv("VTU_API_KEY")
VTU_USER_ID = os.getenv("VTU_USER_ID")
BASE_CALLBACK = os.getenv("BASE_URL")

@router.post("/")
async def buy_electricity(request: Request):
    data = await request.json()
    disco = data["company"]
    meter_type = data["type"]
    meter_no = data["meter"]
    amount = data["amount"]
    phone = data["phone"]
    request_id = str(uuid.uuid4())

    url = "https://www.nellobytesystems.com/APIElectricityV1.asp"
    params = {
        "UserID": VTU_USER_ID,
        "APIKey": VTU_API_KEY,
        "ElectricCompany": disco,
        "MeterType": meter_type,
        "MeterNo": meter_no,
        "Amount": amount,
        "PhoneNo": phone,
        "RequestID": request_id,
        "CallBackURL": f"{BASE_CALLBACK}/electricity/callback"
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()
