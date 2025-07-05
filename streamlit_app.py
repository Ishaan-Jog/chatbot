import streamlit as st
import google.generativeai as genai
import time, os

# Set page layout
st.set_page_config(
    page_title="ChatBot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([8, 1])

with col1:
    st.markdown("# ChatBot 🤖")

with col2:
    # Trash icon with tooltip
    clear = st.button("🗑️", help="Clear Chat", key="clear_btn")

# Clear chat logic
if clear:
    st.session_state.messages = []
    st.success("Chat cleared. You can refresh the page if you want ChatBot to forget the previous conversation.")
    st.rerun()  # Refresh to clear UI

# Configure the model
api_key = st.secrets.get("API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please set GOOGLE_API_KEY environment variable on your system.")
else:
    genai.configure(api_key=api_key)

if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.5-flash")
    st.session_state.chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "You are a chatbot named ChatBot. Speak in a friendly, Gen-Z tone. Be helpful, casual, and slightly witty. Answer clearly and keep responses short unless asked to explain in detail."
            ]  # you may change this for personalization
        }
    ])
if "messages" not in st.session_state:
    st.session_state.messages = []

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
