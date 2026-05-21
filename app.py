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
        reply = "A simple way to manage your salary is by following the 50-30-20 budgeting rule. Use 50% of your money for basic needs like food and travel, 30% for personal spending, and try to save at least 20% every month."

    elif "save" in user_message or "saving" in user_message:
        reply = "If you want to save money effectively, first track where your money is going every day. Avoid unnecessary shopping and try saving a fixed small amount every month."

    elif "expense" in user_message or "shopping" in user_message:
        reply = "Your expenses can become difficult to manage if you spend without planning. Set a weekly spending limit and avoid impulse purchases."

    elif "spending" in user_message:
        reply = "To stop unnecessary spending, wait one day before buying anything non-essential. This helps you avoid impulse buying."

    elif "investment" in user_message:
        reply = "If you are a beginner, start with low-risk investments and first learn basic financial planning. Never invest money without understanding the risks."

    elif "tips" in user_message or "beginner" in user_message:
        reply = "Here are simple financial tips for beginners: First, track your daily expenses. Second, create a monthly budget. Third, save a fixed amount every month. Fourth, avoid unnecessary shopping. Fifth, keep emergency savings for future needs."

    else:
        reply = "I can help you with budgeting, saving money, expense control, beginner financial tips, and simple money management."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
