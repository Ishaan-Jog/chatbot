import streamlit as st
import google.generativeai as genai
import time

# Configure the model
my_api_key = "API_KEY"  # enter your API key
genai.configure(api_key=my_api_key)

if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.5-flash")
    st.session_state.chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "You are a chatbot named ChatBot. Speak in a friendly, Gen-Z tone. Be helpful, casual, and slightly witty. Answer clearly and keep responses short unless asked to explain in detail."
            ]
        }
    ])
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Gemini ChatBot 🤖")

# Show past chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# New message input
prompt = st.chat_input("Ask me anything...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = st.session_state.chat.send_message(prompt)
    reply = response.text if response.candidates and response.candidates[0].content.parts else "⚠️ No reply."

    # Assistant typing animation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        animated_reply = ""
        for word in reply.split(" "):
            animated_reply += word + " "
            display_text = animated_reply.replace("\n", "  \n") + "▌"
            message_placeholder.markdown(display_text)
            time.sleep(0.1)
        message_placeholder.markdown(animated_reply.replace("\n", "  \n"))

    # Save final reply for history
    st.session_state.messages.append({"role": "assistant", "content": reply})
