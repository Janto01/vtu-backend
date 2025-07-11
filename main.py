from fastapi import FastAPI, Request
from routers import airtime, data, cabletv, electricity, betting, wallet, webhook
import telegram
import os

app = FastAPI()

# Include all service routers
app.include_router(airtime.router)
app.include_router(data.router)
app.include_router(cabletv.router)
app.include_router(electricity.router)
app.include_router(betting.router)
app.include_router(wallet.router)
app.include_router(webhook.router)

# Telegram bot setup
bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))

@app.post("/telegram")
async def telegram_webhook(req: Request):
    data = await req.json()
    message = data.get("message", {}).get("text", "")
    chat_id = data.get("message", {}).get("chat", {}).get("id", "")

    if message == "/start":
        await bot.send_message(chat_id, "Welcome to VTU Bot!")

    elif message.startswith("/balance"):
        await bot.send_message(chat_id, "Checking your balance...")

    return {"ok": True}

@app.get("/")
def home():
    return {"status": "online", "message": "VTU backend is running"}
