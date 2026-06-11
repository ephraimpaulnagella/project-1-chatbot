print("🤖 Chatbot Started! Type 'exit' to stop.\n")

name = ""

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello"]:
        print("Bot: Hello! 👋")

    elif "my name is" in user:
        name = user.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you {name}!")

    elif "what is my name" in user:
        if name:
            print(f"Bot: Your name is {name}")
        else:
            print("Bot: I don't know your name yet.")

    elif user in ["how are you"]:
        print("Bot: I'm just code, but I'm doing great! 😄")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")