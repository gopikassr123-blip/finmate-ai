from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Chat Route
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "").lower()

    # Budget Questions
    if "budget" in user_message or "salary" in user_message:

        reply = "A simple way to manage your salary is by following the 50-30-20 budgeting rule. Use 50% of your money for basic needs like food and travel, 30% for personal spending, and try to save at least 20% every month."

    # Saving Money
    elif "save" in user_message or "saving" in user_message:

        reply = "If you want to save money effectively, first track where your money is going every day. Avoid unnecessary online shopping and try saving a fixed small amount every month. Even small savings become useful in the future."

    # Expense / Shopping
    elif "expense" in user_message or "shopping" in user_message:

        reply = "Your expenses can become difficult to manage if you spend without planning. Try setting a weekly spending limit and avoid impulse purchases. Tracking expenses regularly helps you control unnecessary spending."

    # Spending Control
    elif "spending" in user_message:

        reply = "To stop unnecessary spending, avoid buying things immediately when you see offers online. Wait for one day before purchasing anything non-essential. This simple habit can help you save a lot of money."

    # Investment
    elif "investment" in user_message:

        reply = "If you are a beginner, start with low-risk investments and first learn basic financial planning. Never invest money without understanding the risks involved."

    # Default Reply
    else:

        reply = "FinMate AI can help you with budgeting, saving money, expense management, and basic financial guidance for students and beginners."

    return jsonify({
        "reply": reply
    })

# Run Flask App
if __name__ == "__main__":
    app.run()
