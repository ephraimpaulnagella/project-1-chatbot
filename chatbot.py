import datetime

print("🤖 Smart Chatbot Started! Type 'exit' to stop.\n")

name = ""
mood = ""

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def chatbot_response(user):
    global name, mood

    if user in ["hi", "hello", "hey"]:
        return "Hello! 👋 How can I help you?"

    elif "my name is" in user:
        name = user.replace("my name is", "").strip().title()
        return f"Nice to meet you, {name}! 😊"

    elif "what is my name" in user:
        return f"Your name is {name}" if name else "I don't know your name yet."

    elif "how are you" in user:
        return "I'm doing great! Thanks for asking 😄"

    elif "i am feeling" in user:
        mood = user.replace("i am feeling", "").strip()
        return f"I understand you're feeling {mood}. I'm here for you!"

    elif "time" in user:
        return f"Current time is {get_time()} ⏰"

    elif "help" in user:
        return "You can ask me about greetings, your name, time, or tell me how you feel."

    elif user in ["bye", "exit"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Hmm... I didn't understand that. Try asking something else!"

while True:
    user_input = input("You: ").lower()
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input in ["bye", "exit"]:
        break