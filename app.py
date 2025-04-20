from fastapi import FastAPI,Form
from utils.utils import send_message
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def index():
    return {"msg": "up & running"}

@app.post("/message")
async def reply(Body: str):
    # Call the OpenAI API to generate text with GPT-3.5
    try:
        print(Body)

        send_message(os.getenv('TO_NUMBER'), f'Hola\n{Body}')
        return "HolaReturn"
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)