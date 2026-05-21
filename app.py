from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "budget" in user_message or "salary" in user_message:
        reply = "FinMate AI Suggestion: Follow the 50-30-20 budgeting rule. Use 50% for needs, 30% for wants, and 20% for savings."
    elif "save" in user_message or "saving" in user_message:
        reply = "FinMate AI Suggestion: Track your daily expenses regularly and save a fixed amount every month."
    elif "expense" in user_message or "shopping" in user_message:
        reply = "FinMate AI Suggestion: Reduce unnecessary shopping and maintain a weekly spending limit."
    elif "investment" in user_message:
        reply = "FinMate AI Suggestion: Start with low-risk investments and learn basic financial planning before investing."
    else:
        reply = "FinMate AI can help you with budgeting, saving tips, expense analysis, and student financial management."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
