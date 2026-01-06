from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime  # <--- 1. IMPORT THIS

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # 2. GET CURRENT DATE
        current_date = datetime.now().strftime("%B %d, %Y")
        
        # 3. INJECT INTO SYSTEM PROMPT
        # We insert a system message at the VERY START of the list
        system_instruction = {
            "role": "system", 
            "content": f"You are a helpful AI assistant. Today's date is {current_date}. Answer questions based on this date."
        }
        
        # Combine system instruction + conversation history
        final_messages = [system_instruction] + request.messages

        chat_completion = client.chat.completions.create(
            messages=final_messages,
            model="llama-3.1-8b-instant",
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))