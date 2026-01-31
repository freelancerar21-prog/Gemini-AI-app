# ফাইলের শুরুতে (লাইন ৭-৮)
API_KEY = os.environ.get("XAI_API_KEY") # এখানে Render-এ দেওয়া নাম ব্যবহার করুন
URL = "https://api.groq.com/openai/v1/chat/completions"

# চ্যাট ফাংশনের ভেতরে (লাইন ৬৬ থেকে ৭০ এর আশেপাশে)
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    headers = {
        "Authorization": f"Bearer {API_KEY}", # এখানে ভ্যারিয়েবল নাম সঠিক করুন
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mixtral-8x7b-32768", # অথবা আপনার পছন্দের Groq মডেল
        "messages": [{"role": "user", "content": user_message}]
    }
    
    r = requests.post(URL, headers=headers, json=data)
    
    # এরর হ্যান্ডলিং যোগ করুন যাতে ক্রাশ না করে
    try:
        response_json = r.json()
        reply = response_json['choices'][0]['message']['content']
    except (KeyError, IndexError, ValueError):
        reply = f"দুঃখিত, সমস্যা হয়েছে। সার্ভার রেসপন্স: {r.text}"
        
    return jsonify({"reply": reply})
    
