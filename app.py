from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Paste your Gemini API Key here
genai.configure(api_key="AIzaSyB6muXHtZX9nRaD3-Y9W-7PN05dwbAHz_U")

# Gemini Model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Chat Route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        user_message = data["message"]

        prompt = f"""
        You are FinMate AI, a smart finance chatbot.

        Help users with:
        - budgeting
        - saving money
        - expense analysis
        - financial advice for students
        - monthly planning

        Give short and simple answers.

        User Message:
        {user_message}
        """

        response = model.generate_content(prompt)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
    return jsonify({
        "reply": "💰 FinMate AI Suggestion:\n\nTry following the 50-30-20 budgeting rule.\n\n50% for needs\n30% for wants\n20% for savings.\n\nAlso reduce unnecessary shopping and track daily expenses regularly."
    })

# Run App
if __name__ == "__main__":
    app.run(debug=True)