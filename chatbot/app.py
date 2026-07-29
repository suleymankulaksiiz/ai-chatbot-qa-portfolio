from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise Exception("OPENAI_API_KEY bulunamadı")


client = OpenAI(
    api_key=api_key
)


app = FastAPI(
    title="AI Chatbot API",
    description="Simple AI chatbot for QA testing portfolio",
    version="1.0"
)


class ChatRequest(BaseModel):

    message: str



@app.get("/")
def home():

    return {
        "status": "AI Chatbot API is running"
    }



@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ],

        temperature=0

    )


    answer = response.choices[0].message.content


    return {

        "answer": answer

    }