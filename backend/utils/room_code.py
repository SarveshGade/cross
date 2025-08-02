import random
import string

def generate_room_code(length: int=4):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

