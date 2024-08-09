import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me ChatGPT.",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you!", "I'm a bot, so I don't have feelings, but I'm here to help!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no problem.", "No worries!",]
    ],
    [
        r"I need (.*)",
        ["Why do you need %1?", "Are you sure you need %1?",]
    ],
    [
        r"quit",
        ["Bye for now! Have a great day.", "Goodbye! It was nice talking to you."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Could you please rephrase?"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to initiate chat
def chat():
    print("Hi! I am a chatbot. Type 'quit' to exit the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Bot: {response}")

# Start chatting
if __name__ == "__main__":
    chat()




