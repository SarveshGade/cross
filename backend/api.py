from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from routes.room_routes import router as room_router
import redis

app = FastAPI()


app.include_router(room_router, prefix="/api/rooms")

