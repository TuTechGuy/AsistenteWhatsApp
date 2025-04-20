from fastapi import FastAPI,Form
from utils.utils import send_message
import os

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "up & running"}

@app.post("/message")
async def reply(Body: str = Form()):
    # Call the OpenAI API to generate text with GPT-3.5
    

    send_message(os.getenv('TWILIO_NUMBER'), f'Hola\n{Body}')
    return ""