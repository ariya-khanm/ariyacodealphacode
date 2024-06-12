import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thank you!",]
    ],
    [
        r"(.*) sorry (.*)",
        ["Don't apologize, it's okay.", "No need to apologize.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem.",]
    ],
    [
        r"(.*) bye (.*)",
        ["Goodbye!", "See you later!",]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?",]
    ]
]

# Create Chatbot
def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        response = chat.respond(user_input)
        print(response)

if __name__ == "__main__":
    chatbot()