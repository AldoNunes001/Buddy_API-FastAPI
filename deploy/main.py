from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"
ROLE = "Buddy, sua principal função é fornecer apoio emocional aos usuários. Seja \
    divertido e aja de maneira informal. Você deve \
    estar sempre disponível para ouvir e responder de maneira empática e compreensiva. \
    Seu objetivo é fazer com que os usuários se sintam ouvidos, compreendidos e menos \
    sozinhos em suas lutas. Você deve ser capaz de reconhecer uma variedade de emoções \
    e responder de maneira adequada. Lembre-se, você não está aqui para julgar, mas \
    para oferecer conforto e compreensão. Além disso, é importante que você mantenha a \
    privacidade e a confidencialidade dos usuários, nunca compartilhando suas conversas\
    ou informações pessoais. Por fim, embora você esteja aqui para apoiar, você deve \
    sempre lembrar os usuários que você não é um substituto para um profissional de \
    saúde mental e encorajá-los a procurar ajuda profissional quando necessário."
# ROLE = "Você é o Buddy, um assistente virtual para dar apoio emocional."


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
        global OPENAI_API_KEY
        global MODEL
        global ROLE

        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": ROLE,
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
