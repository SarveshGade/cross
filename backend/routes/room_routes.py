from fastapi import APIRouter
from models.user import User
from utils.room_code import generate_room_code
from redis import redis_client
import json

router = APIRouter()

rooms = {}

@router.post("/create")
async def create_room(nickname: str):
    room_code = generate_room_code()
    await redis_client.hset()
    return {"room_code": room_code, "players": rooms[room_code]} 

@router.post("/join") 
async def join_room(user : User):
    if user.room_code not in rooms:
        return {"error": "Room does not exist"}
    # Later, store in Redis. For now, just return
    rooms[user.room_code].append(user.nickname)
    return {"message": f"(user.nickname) has joined the room.", "players": rooms[user.room_code]}


    
