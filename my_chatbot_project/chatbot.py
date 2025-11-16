
import google.generativeai as genai
from google.colab import userdata # Import userdata to securely fetch API key

genai.configure(api_key='AIzaSyB0Ja844f3EWoBSDAZxRS9zL4BWNGVwShY')

def generate_response(user_message, chat_history=[]):
    conversation = []
    for role, text in chat_history:
        conversation.append({"role": role, "parts": [text]})
    conversation.append({"role": "user", "parts": [user_message]})
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(conversation)
    return response.text
