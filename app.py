import streamlit as st
from openai import OpenAI

# আপনার API Key সরাসরি এখানে বসানো হয়েছে
API_KEY = "Xai-PgC4XkV7PEoJ0bR7CGvsvOeuOCLPBtf6HQHTXKKN8a8oM9jUO5Cu9ouqScH6RwTlatxZxgracrrpoHIr"

st.set_page_config(page_title="My Grok AI", page_icon="🤖")
st.title("Grok AI Chatbot")

# Client Setup
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.x.ai/v1",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Grok-কে কিছু জিজ্ঞাসা করুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="grok-2", 
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            )
            answer = response.choices[0].message.content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Error: {e}")
            
