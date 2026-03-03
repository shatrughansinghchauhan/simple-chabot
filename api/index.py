from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define simple rules for the chatbot
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I am a program, so I'm doing well, thank you!", "Doing great in binary!"],
    "bye": ["Goodbye! Have a great day.", "See ya! Come back soon."],
    "default": ["Tell me more.", "Why do you say that?", "Interesting... go on."]
}

def get_bot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    # Note: Vercel runs the app differently; this is for local testing.
    app.run(debug=True)
