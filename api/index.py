from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    # Basic chatbot logic: respond to "hello" or anything else
    if user_message.lower() == "hello":
        bot_reply = "Hi there! How can I help you today?"
    else:
        bot_reply = f"You said: '{user_message}'. I'm a simple bot and don't understand much yet."
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    # Note: Vercel runs the app differently; this is for local testing.
    app.run(debug=True)
