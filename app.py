import streamlit as st
import google.generativeai as genai

# সরাসরি আপনার দেওয়া Gemini API Key
API_KEY = "AIzaSyDInMEDhlsfBhTnpE3VW7TdC9Y7mzLDnpY"

# পেজ সেটিংস
st.set_page_config(page_title="My Personal AI", page_icon="🚀")
st.title("Gemini 3 Flash AI Bot")

# Google Generative AI কনফিগারেশন (v1 স্ট্যাবল ভার্সন)
genai.configure(api_key=API_KEY)

# ২০২৬ সালের লেটেস্ট এবং দ্রুততম মডেল ব্যবহার করা হয়েছে
model = genai.GenerativeModel('gemini-3-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# চ্যাট স্ক্রিন প্রদর্শন
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট
if prompt := st.chat_input("আপনি কী জানতে চান?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # এআই রেসপন্স জেনারেশন
            response = model.generate_content(prompt)
            answer = response.text
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            # মডেল না পাওয়া গেলে বা অন্য এরর হলে এখানে দেখাবে
            st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
