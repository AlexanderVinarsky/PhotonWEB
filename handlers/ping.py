from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["Ping"])

@router.get("/db")
async def ping_db():
    return {"message": "pong"}

@router.get("/app")
async def ping_app():
    return {"text": "app is working"}