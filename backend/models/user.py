from pydantic import BaseModel

class User(BaseModel):
    nickname:str
    room_code : str
    
