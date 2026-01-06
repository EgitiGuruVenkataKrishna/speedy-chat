# ⚡ Speedy Agent

**Speedy Agent** is a full-stack AI chat application designed for high-velocity inference and conversational memory. Unlike standard wrappers, this project implements a decoupled **Client-Server Architecture** using FastAPI for the backend intelligence and Streamlit for the frontend interface.

## 🚀 Key Features
* **Groq Inference Engine:** Utilizes Llama-3 via Groq API for near-instant text generation ( < 100ms latency).
* **Persistent Context:** Implements a custom memory buffer in the frontend state, allowing the model to recall previous turns in the conversation.
* **Separation of Concerns:** Distinct backend logic (API) and frontend presentation (UI) mimicking production-grade microservices.
* **Dynamic System Prompting:** Injects real-time context (Date/Time) into the model's system prompt on every request.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** Streamlit
* **AI Model:** Llama-3-8b (via Groq)
* **Utilities:** Pydantic (Data Validation), Python-Dotenv (Security)

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/EgitiGuruVenkataKrishna/speedy-chat.git](https://github.com/EgitiGuruVenkataKrishna/speedy-chat.git)
cd speedy-chat