from fastapi import FastAPI,Form
from utils.utils import send_message
import uvicorn
import os
from pydantic import BaseModel

app = FastAPI()
class Request(BaseModel):
    To: str
    Body: str
    From: str


@app.get("/")
async def index():
    return {"msg": "up & running"}

@app.post("/message")
async def reply(request: Request):
    # Call the OpenAI API to generate text with GPT-3.5
    try:

        send_message(os.getenv('TO_NUMBER'), f'Hola\n{request.Body}\n{request.From}\n{request.To}')
        return "HolaReturn"
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)