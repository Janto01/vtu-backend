from fastapi import APIRouter, Request
import httpx
import os
import uuid

router = APIRouter(prefix="/cabletv", tags=["Cable TV"])

VTU_API_KEY = os.getenv("VTU_API_KEY")
VTU_USER_ID = os.getenv("VTU_USER_ID")
BASE_CALLBACK = os.getenv("BASE_URL")

@router.post("/")
async def buy_cabletv(request: Request):
    data = await request.json()
    cabletv = data["cabletv"]
    package = data["package"]
    smartcard = data["smartcard"]
    phone = data["phone"]
    request_id = str(uuid.uuid4())

    url = "https://www.nellobytesystems.com/APICableTVV1.asp"
    params = {
        "UserID": VTU_USER_ID,
        "APIKey": VTU_API_KEY,
        "CableTV": cabletv,
        "Package": package,
        "SmartCardNo": smartcard,
        "PhoneNo": phone,
        "RequestID": request_id,
        "CallBackURL": f"{BASE_CALLBACK}/cabletv/callback"
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()
