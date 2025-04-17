import random
import string
response_map = {
    ("hi", "hello", "hey"): "Hello! Welcome to Cafe How can I help you today?",
    ("what do you serve", "menu", "food", "drink"): "We serve freshly coffee , tea and delicious pastries ",
    ("credit card", "paypal", "payment"): "Yes! We accept all major credit cards, UPI, and PayPal.",
    ("thanks", "thank you", "alright got it"): "You're welcome! Let me know if you need anything else.",
    ("bye", "quit", "exit"): "Goodbye! Hope to serve you again soon"
}
default_responses = [
    "I'm not sure about that. Maybe ask about our menu or payment options?",
    "Sorry, I didn’t get that. Would you like to see our menu?",
    "Hmm… I’m still learning. Try asking me what we serve!",
    "You can ask me about drinks, payments, or anything café-related "
]

def clean_input(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text
print("Bot: Hello! What's your name?")
user_name = input("You: ")
print(f"Bot: Nice to meet you, {user_name}! Welcome to Cafe")
print("Bot: Ask me anything about our menu, drinks, or payment options. Type 'bye' to leave the chat.")

while True:
    user_input = input("You: ")
    cleaned_input = clean_input(user_input)

    found = False

    for keywords, response in response_map.items():
        for word in keywords:
            if word in cleaned_input:
                print("Bot:", response)
                found = True
                break
        if found:
            break

    if not found:
        print("Bot:", random.choice(default_responses))

    if "bye" in cleaned_input or "quit" in cleaned_input or "exit" in cleaned_input:
        break
