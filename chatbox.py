import random
import nltk

# ---------- CONFIG ----------
DEBUG = True                    # set to False once everything works
EXIT_WORD = "exit"              # how to quit the chat
# -----------------------------

intents = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "hii", "hola"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see", "later"],
        "responses": ["Good‑bye!", "See you later!", "Bye!"]
    },
    "thanks": {
        "keywords": ["thanks", "thank", "thx"],
        "responses": ["You’re welcome 😊", "Anytime!", "Glad to help!"]
    },
    "name": {
        "keywords": ["your", "name", "who", "are"],
        "responses": ["I’m a simple chatbot created by Arpita!"]
    },
    "joke": {
        "keywords": ["joke", "funny", "laugh"],
        "responses": ["Why did the Python programmer go broke? Because he couldn’t C#! 😂"]
    },
    "age": {
        "keywords": ["age", "old"],
        "responses": ["I’m timeless — I came alive when you ran the script!"]
    }
}

def detect_intent(user_input: str) -> str:
    """Return the best‑matched intent or 'unknown'."""
    tokens = user_input.lower().split()        # simple, reliable tokenizer
    if DEBUG: print("  🐞 tokens:", tokens)

    for intent, data in intents.items():
        if any(word in tokens for word in data["keywords"]):
            if DEBUG: print(f"  🐞 matched intent: {intent}")
            return intent
    if DEBUG: print("  🐞 matched intent: unknown")
    return "unknown"

def reply_for_intent(intent: str) -> str:
    if intent in intents:
        return random.choice(intents[intent]["responses"])
    return "I’m not sure I understand. Could you rephrase?"

def start_chat():
    print("🤖 Chatbot: Hello! (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == EXIT_WORD:
            print("🤖 Chatbot: Bye!")
            break

        intent = detect_intent(user_input)
        response = reply_for_intent(intent)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    start_chat()
