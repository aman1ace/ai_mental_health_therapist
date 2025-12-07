from fastapi import FastAPI
from pydantic import BaseModel
from backend.ai_agent import SYSTEM_PROMPT, chat_with_groq

import os
os.environ["GROQ_API_KEY"] = ""


app = FastAPI()


class Query(BaseModel):
    message: str


@app.post("/ask")
async def ask(query: Query):
    reply = chat_with_groq(query.message)
    return {"response": reply}


# Run manually using:
# uv run uvicorn backend.main:app --reload --port 8000
