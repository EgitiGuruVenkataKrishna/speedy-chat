import streamlit as st
import requests

st.title("🧠 Memory Agent")

# 1. Initialize Chat History if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Handle New Input
if prompt := st.chat_input("What is up?"):
    # Add User message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 4. Send FULL History to Backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "https://speedy-agent-api.onrender.com/chat", 
                    json={"messages": st.session_state.messages} # Sending the whole conversation
                )
                
                if response.status_code == 200:
                    ai_response = response.json().get("response")
                    st.markdown(ai_response)
                    # Add AI response to history
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection Error: {e}")