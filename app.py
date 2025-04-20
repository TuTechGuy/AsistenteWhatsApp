from fastapi import FastAPI,Form
from utils.utils import send_message
import uvicorn
import os
from pydantic import BaseModel
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
client = AzureOpenAI(api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
                     api_key=os.getenv('AZURE_OPENAI_API_KEY'),
                     azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')),

@app.get("/")
async def index():
    return {"msg": "up & running"}

@app.post("/message")
async def reply(Body: str = Form(...),From: str = Form(...)):
    # Call the OpenAI API to generate text with GPT-3.5
    try:
        response = client.chat.completions.create(
            model=os.getenv('AZURE_OPENAI_MODEL'),
            messages=[
                {"role": "user", "content": Body}
            ],
            max_tokens=100,
            temperature=0.7
        )
        respuesta = response.choices[0].message.content
        send_message(From, respuesta)
        return "HolaReturn"
    except Exception as e:
        print(f"Error: {e}")
        return "Error"

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)