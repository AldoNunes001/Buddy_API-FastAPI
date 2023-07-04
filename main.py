from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class Message(BaseModel):
    content: str


@app.post("/chat", response_model=Message)
async def chat_endpoint(message: Message):
    async with httpx.AsyncClient() as client:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "Voce é o Buddy, um assistente virtual para dar\
                        apoio emocional",
                },
                {
                    "role": "user",
                    "content": message.content,
                },
            ],
        }

        global OPENAI_API_KEY
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        }

        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            json=data,
            headers=headers,
        )

        if response.status_code != 200:
            # print(f"Error: {response.status_code}, {response.text}")
            return {"content": "Houve um erro ao processar sua mensagem"}

        response_data = response.json()
        chatbot_message = response_data["choices"][0]["message"]["content"]

        return {"content": chatbot_message}
