from collections import Counter

def generate_dashboard(chat_history):

    sentiments = Counter()
    intents = Counter()

    for chat in chat_history:
        sentiments[chat["sentiment"]] += 1
        intents[chat["intent"]] += 1

    return {
        "total_chats": len(chat_history),
        "sentiments": dict(sentiments),
        "intents": dict(intents)
    }