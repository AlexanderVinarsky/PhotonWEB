import string

from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all")
async def get_tasks():
    return {"message": "pong"}

@router.post("/")
async def create_task():
    return {"text": "app is working"}

@router.put("/{task_id}")
async def update_task(task_id: int):
    return {"text": f"task updated {task_id}"}

@router.patch("/{task_id}")
async def patch_task(task_id: int, name: str):
    return {"text": f"task patched {task_id}"}