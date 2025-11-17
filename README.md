🌟 Gemini Chatbot — AI-Powered Conversational App

An interactive chatbot built using **Google Gemini API**, **Streamlit**, and **Python**.
This project demonstrates how to integrate LLMs into a real-time web application with clean modular architecture.

---

## 🚀 Features

✔ **Conversational AI** using Google Gemini
✔ **Streamlit UI** for real-time chatting
✔ **Modular Code Structure** (`chatbot.py` for model logic, `app.py` for UI)
✔ **Ngrok Integration** to run the app publicly from Google Colab

---

## 📁 Project Structure

```
my_chatbot_project/
│
├── chatbot.py        # Handles Gemini API calls and response generation
├── app.py            # Streamlit frontend (UI + app logic)
```

---

## 🔧 Technologies Used

* **Python 3**
* **Streamlit**
* **Google Gemini API**
* **PyNgrok** (for exposing the app publicly)
* **Google Colab / VS Code (optional)**

---

## 🔑 Setup Instructions

### 1️⃣ Install Dependencies

```
!pip install google-generativeai streamlit pyngrok
```

### 2️⃣ Set up Gemini API Key

Create an environment variable:

```
export GEMINI_API_KEY="your_api_key_here"
```

or on **Windows**:

```
set GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the App

### **Local Machine**

```
streamlit run app.py
```

### **From Colab Using Ngrok**

Run:

```
!streamlit run app.py & npx localtunnel --port 8501
```

Or using PyNgrok:

```
from pyngrok import ngrok
public_url = ngrok.connect(8501)
```

---

## 💡 How It Works

### **1. User enters a message in Streamlit**

Streamlit passes it to `generate_response()` inside `chatbot.py`.

### **2. Gemini receives the prompt**

The Google LLM processes the chat history + new message.

### **3. Streamlit displays the model output**

Chat history updates and repeats.

