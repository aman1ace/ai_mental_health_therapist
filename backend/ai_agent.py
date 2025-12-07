from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()  # <— THIS WILL LOAD .env INTO THE PROCESS
GROQ_API_KEY = os.getenv(
    " ")


# System prompt for your AI therapist
SYSTEM_PROMPT = """
You are a supportive mental health companion. 
Provide calm, empathetic, and supportive responses.
Avoid giving medical or legal advice.
"""

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # Fast + free
    temperature=0.4,
    api_key=os.getenv(
        " ")
)


def chat_with_groq(user_message: str) -> str:
    messages = [
        ("system", SYSTEM_PROMPT),
        ("user", user_message)
    ]

    response = llm.invoke(messages)
    return response.content
