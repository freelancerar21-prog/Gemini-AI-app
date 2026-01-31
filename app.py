import streamlit as st
import google.generativeai as genai

# সরাসরি আপনার দেওয়া API Key
API_KEY = "AIzaSyDInMEDhlsfBhTnpE3VW7TdC9Y7mzLDnpY"

st.set_page_config(page_title="My Gemini AI", page_icon="🤖")
st.title("Gemini 1.5 Flash Chatbot")

# Google Generative AI কনফিগারেশন
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("আপনি কী জানতে চান?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # এআই থেকে উত্তর জেনারেট করা
            response = model.generate_content(prompt)
            answer = response.text
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
            
