
# Buddy: Emotional Support Chatbot API

This repository hosts the code for Buddy, a simple FastAPI application that serves as an emotional support chatbot API. The chatbot uses the OpenAI's GPT-3.5-turbo language model to generate conversational responses.


## Dependencies

To run this project, you will need the following dependencies installed:
- FastAPI
- Pydantic
- httpx
- python-dotenv
- Python 3.7 or above

You can install the dependencies by running:

```bash
   pip install "fastapi[all]" python-dotenv
```


## Environment Variables

The application uses the python-dotenv package to load environment variables. You need to create a .env file in the root directory and define the following variable:

- **`OPENAI_API_KEY`**: Your OpenAI API key.

## Run Locally

Clone the project

```bash
  git clone https://github.com/AldoNunes001/Buddy_API-FastAPI.git
```

Go to the project directory

```bash
  cd Buddy_API-FastAPI
```

Install dependencies

```bash
  pip install "fastapi[all]" python-dotenv
```

Start the server

```bash
  uvicorn main:app --reload
```


## API Endpoints

#### POST /chat

Generates a conversational response using the GPT-3.5-turbo model.

#### Request Body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `str` | **Required**. A unique identifier for the conversation. |
| `user_penultimate_message` | `str` | **Required**. The second to last message from the user. |
| `buddy_last_message` | `str` | **Required**. The last message from Buddy, the chatbot. |
| `user_last_message` | `str` | **Required**. The last message from the user. |

#### Response Body

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `content`      | `str` | A string containing the response generated by the chatbot. |

## Disclaimer

**Buddy Bot Legal Notice**

The Buddy Bot was designed to provide an interactive interface that responds and provides support in situations where the user may need company to talk to. The Buddy Bot can offer automatic responses with the intention of helping to provide some comfort or temporary relief.

Please be aware that:

  1. The Buddy Bot is not a licensed mental health professional, nor a counselor, psychologist, or psychiatrist. It does not provide medical advice, diagnoses, or treatments.

  2. The responses provided by the Buddy Bot should not be used as a substitute for professional advice. If you are going through a crisis or if you or someone else is in danger, please contact a mental health professional, a competent authority, or, in Brazil, call the Lifeline at 188, which provides emotional support 24/7, or visit the website https://www.cvv.org.br/.

  3. The Buddy Bot does not have the ability to interpret crisis situations, medical or mental health emergencies, or provide real-time assistance.

  4. All interactions with the Buddy Bot are based on artificial intelligence, which means that the responses are automatically generated and are not monitored by humans in real time.

  5. We respect your privacy. All conversations with the Buddy Bot are anonymous, and we do not collect, store, or share any personal data of the user. Our goal is to provide a safe space for you to express yourself.

By using the Buddy Bot, you agree to this Legal Notice and understand that any action or decision made based on the Buddy Bot's responses is entirely your responsibility.



