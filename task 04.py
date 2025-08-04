import random

def simple_chatbot():
    """
    A simple rule-based chatbot that responds to user input.
    """
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    how_are_you_questions = ["how are you", "how are you doing", "how's it going"]

    # Predefined replies
    greeting_replies = ["Hi there!", "Hello!", "Hey! What can I do for you?", "Greetings!"]
    farewell_replies = ["Goodbye!", "See you later!", "Talk to you soon!", "Bye! Take care."]
    how_are_you_replies = ["I'm doing great, thank you for asking!", "I'm fine, thanks!", 
                           "All good! How about you?", "I'm just a program, but I'm operating perfectly!"]
    
    # A list of general predefined responses for other topics
    general_replies = {
        "name": ["I am a simple chatbot, you can call me Bot.", "You can call me Python Chatbot.", "I don't have a name, but you can give me one!"],
        "weather": ["I can't check the weather, but I hope it's a nice day!", "Weather is not my specialty, but I'm sure it's lovely."],
        "thanks": ["You're welcome!", "My pleasure!", "Anytime!"],
        "help": ["I can answer simple questions about greetings and how I'm doing.", "I'm a simple bot, so my abilities are limited."]
    }

    # Default responses for unrecognized input
    default_replies = ["I'm not sure how to respond to that.", "Could you rephrase that?",
                       "That's an interesting topic.", "I don't have a predefined response for that."]
    
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        # Check for farewell
        if any(word in user_input for word in farewells):
            print("Chatbot:", random.choice(farewell_replies))
            break
        
        # Check for greetings
        if any(word in user_input for word in greetings):
            print("Chatbot:", random.choice(greeting_replies))
        # Check for "how are you" questions
        elif any(phrase in user_input for phrase in how_are_you_questions):
            print("Chatbot:", random.choice(how_are_you_replies))
        # Check for other predefined topics
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatbot:", random.choice(general_replies["name"]))
        elif "weather" in user_input:
            print("Chatbot:", random.choice(general_replies["weather"]))
        elif "thank" in user_input:
            print("Chatbot:", random.choice(general_replies["thanks"]))
        elif "help" in user_input:
            print("Chatbot:", random.choice(general_replies["help"]))
        # Default response for unrecognized input
        else:
            print("Chatbot:", random.choice(default_replies))

if __name__ == "__main__":
    simple_chatbot()