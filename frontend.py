# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 AI Mental Health Therapist")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step2: User input
user_input = st.chat_input("What's on your mind today?")

if user_input:
    # Add user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    # Send to backend
    response = requests.post(BACKEND_URL, json={"message": user_input})
    data = response.json()

    # Safe access
    tool = data.get("tool_called", None)
    tool_text = f" WITH TOOL [{tool}]" if tool else ""

    # Add assistant message
    st.session_state.chat_history.append(
        {"role": "assistant", "content": data["response"] + tool_text}
    )


# Step3: Display chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
