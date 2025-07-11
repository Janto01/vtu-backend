from fastapi import FastAPI, Request
from routers import airtime, data, cabletv, electricity, betting, wallet, webhook

app = FastAPI()

# Include routers
app.include_router(airtime.router)
app.include_router(data.router)
app.include_router(cabletv.router)
app.include_router(electricity.router)
app.include_router(betting.router)
app.include_router(wallet.router)
app.include_router(webhook.router)

@app.get("/")
def read_root():
    return {"message": "VTU API is live!"}