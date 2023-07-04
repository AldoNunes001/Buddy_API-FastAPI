from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()


# Modelo para o corpo da requisição
class ChatIn(BaseModel):
    message: str


# Modelo para a resposta
class ChatOut(BaseModel):
    response: str


@app.post("/chat", response_model=ChatOut)
async def chat_endpoint(chat_in: ChatIn):
    # Aqui você faria uma chamada para a API GPT com a mensagem de chat_in
    # e obteria a resposta. Para este exemplo, vamos apenas repetir a mensagem.
    chat_out = ChatOut(response=chat_in.message)
    return chat_out
