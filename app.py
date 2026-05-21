from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "PASTE_YOUR_API_KEY_HERE"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },

            json={

                "model": "openrouter/auto",

                "messages": [

                    {
                        "role": "system",
                        "content": "You are FinMate AI, a friendly finance chatbot. Explain financial topics in very simple and clear English like teaching a beginner."
                    },

                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            }
        )

        result = response.json()

        reply = result["choices"][0]["message"]["content"]

    except Exception:

        reply = "Sorry, AI service is currently unavailable."

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run()
