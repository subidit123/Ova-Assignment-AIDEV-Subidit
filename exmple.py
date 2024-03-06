import random

class Chatbot:
    def __init__(self):
        self.greetings = ["Hello", "Hi", "How are you?"]
        self.goodbyes = ["Goodbye", "See you later", "Have a nice day"]
        self.keywords = ["weather", "news", "sports"]
        self.responses = {
            "weather": "The weather today is sunny and warm.",
            "news": "The top news story today is that the president has signed a new bill into law.",
            "sports": "The Yankees won their game last night."
        }

    def greet(self):
        greeting = random.choice(self.greetings)
        print(greeting)

    def goodbye(self):
        goodbye = random.choice(self.goodbyes)
        print(goodbye)

    def respond(self, message):
        for keyword in self.keywords:
            if keyword in message:
                response = self.responses[keyword]
                print(response)

if __name__ == "__main__":
    chatbot = Chatbot()

    chatbot.greet()

    while True:
        message = input("What would you like to talk about? ")

        if message == "bye":
            chatbot.goodbye()
            break

        chatbot.respond(message)