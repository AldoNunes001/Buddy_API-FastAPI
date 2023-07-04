import asyncio
import aiohttp
import json
import random
import string
import time


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

async def make_request(session, url):
    data = {
        "message": generate_random_string(),  # Gera uma mensagem aleatória
    }
    start_time = time.perf_counter()  # Inicia a contagem do tempo
    async with session.post(url, json=data) as resp:
        end_time = time.perf_counter()  # Finaliza a contagem do tempo
        print(f"Request took {end_time - start_time} seconds.")
        return await resp.json()  # Supõe-se que a resposta seja um JSON.

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["http://localhost:8000/chat" for _ in range(1000)]  # 1000 requisições para o endpoint do seu chatbot
        tasks = [make_request(session, url) for url in urls]
        start_time = time.perf_counter()  # Inicia a contagem do tempo total
        responses = await asyncio.gather(*tasks)  # faz as requisições de forma concorrente
        end_time = time.perf_counter()  # Finaliza a contagem do tempo total
        print(responses)  # imprime as respostas
        print(f"Total time taken: {end_time - start_time} seconds.")

asyncio.run(main())
