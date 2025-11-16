
import sys
import os
sys.path.append("/project")  # Ensure /project is in sys.path
os.chdir("/project") # Change working directory for Streamlit to find modules

import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Gemini AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.history.append(("user", user_input))
    bot_reply = generate_response(user_input, st.session_state.history)
    st.session_state.history.append(("model", bot_reply))

for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(text)
