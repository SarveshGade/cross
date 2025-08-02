from fastapi import APIRouter
from models.user import User

router = APIRouter()

@router.post("/join") 
async def join_room(user : User):
    # Later, store in Redis. For now, just return
    return {"message": f"(user.nickname) has joined the room."}
    
