def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Greeting"

    elif any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye"

    elif any(word in text for word in ["thanks", "thank you"]):
        return "Thank You"

    elif "help" in text:
        return "Help"

    else:
        return "General Question"