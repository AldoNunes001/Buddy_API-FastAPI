from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class ChatOut(BaseModel):
    content: str


class ChatIn(BaseModel):
    id: str
    user_penultimate_message: str
    buddy_last_message: str
    user_last_message: str


@app.post("/chat", response_model=ChatOut)
async def chat_endpoint(message: ChatIn) -> ChatOut:
    async with httpx.AsyncClient() as client:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "Você é o Buddy, um assistente virtual para \
                        dar apoio emocional.",
                },
                {
                    "role": "user",
                    "content": message.user_penultimate_message,
                },
                {
                    "role": "assistant",
                    "content": message.buddy_last_message,
                },
                {
                    "role": "user",
                    "content": message.user_last_message,
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
            timeout=30.0,
        )

        if response.status_code != 200:
            # print(f"Error: {response.status_code}, {response.text}")
            return {"content": "Houve um erro ao processar sua mensagem"}

        response_data = response.json()
        chatbot_message = response_data["choices"][0]["message"]["content"]

        return {"content": chatbot_message}
