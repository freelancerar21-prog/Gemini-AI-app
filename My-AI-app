import os
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# আপনার Groq API Key Render-এর Environment Variable-এ সেট করবেন
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"

HTML_UI = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Groq AI Bot</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #f0f2f5; }
        .container { max-width: 500px; margin: 20px auto; display: flex; flex-direction: column; height: 90vh; background: white; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); overflow: hidden; }
        #messages { flex-grow: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; }
        .msg { margin-bottom: 15px; padding: 10px 15px; border-radius: 15px; max-width: 80%; line-height: 1.5; }
        .user { align-self: flex-end; background: #0084ff; color: white; border-bottom-right-radius: 2px; }
        .bot { align-self: flex-start; background: #e4e6eb; color: black; border-bottom-left-radius: 2px; }
        .input-area { display: flex; padding: 15px; border-top: 1px solid #ddd; }
        input { flex-grow: 1; padding: 12px; border: 1px solid #ddd; border-radius: 25px; outline: none; }
        button { padding: 10px 20px; background: #0084ff; color: white; border: none; border-radius: 25px; margin-left: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <div id="messages"></div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Message...">
            <button onclick="send()">Send</button>
        </div>
    </div>
    <script>
        async function send() {
            const input = document.getElementById('userInput');
            const msgDiv = document.getElementById('messages');
            if(!input.value) return;
            
            msgDiv.innerHTML += `<div class="msg user">${input.value}</div>`;
            const text = input.value;
            input.value = '';

            const response = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: text})
            });
            const data = await response.json();
            msgDiv.innerHTML += `<div class="msg bot">${data.reply}</div>`;
            msgDiv.scrollTop = msgDiv.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_UI)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": user_message}]
    }
    r = requests.post(URL, headers=headers, json=data)
    reply = r.json()['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
