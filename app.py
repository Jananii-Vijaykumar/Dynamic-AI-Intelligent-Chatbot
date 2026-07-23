from flask import Flask, render_template, request, jsonify
from chatbot.ai import get_ai_response
from chatbot.memory import save_memory, get_memory
from chatbot.sentiment import analyze_sentiment
from chatbot.ner import extract_entities
from chatbot.intent import detect_intent
from analytics.dashboard import generate_dashboard
import re

app = Flask(__name__)

# Store chat history
chat_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Default values (used for dashboard)
    intent = detect_intent(user_message)
    sentiment = analyze_sentiment(user_message)
    entities = extract_entities(user_message)

    # -------------------------
    # Memory Feature
    # -------------------------
    match = re.search(r"my name is (.+)", user_message.lower())

    if match:
        name = match.group(1).title()
        save_memory("name", name)
        bot_response = f"Nice to meet you, {name}!"

    elif "what is my name" in user_message.lower():
        name = get_memory("name")

        if name:
            bot_response = f"Your name is {name}."
        else:
            bot_response = "I don't know your name yet. Please tell me."

    else:
        # AI Response
        bot_response = get_ai_response(user_message)

    # Save chat history
    chat_history.append({
        "user": user_message,
        "bot": bot_response,
        "intent": intent,
        "sentiment": sentiment,
        "entities": entities
    })

    return jsonify({
        "response": bot_response
    })


@app.route("/dashboard")
def dashboard():
    data = generate_dashboard(chat_history)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)