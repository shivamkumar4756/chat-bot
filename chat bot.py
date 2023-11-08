import random

# Define a dictionary of responses
responses = {
    "hello": ["Hey! I am the chatbot of SkillSync Interns."],
    "how are you": ["I'm good, thanks!", "I'm just a computer program, so I don't have feelings, but I'm here to help!"],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?", "I don't understand."]
}

# Function to generate a response
def generate_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitivity
    if user_input in responses:
        response = random.choice(responses[user_input])
    else:
        response = random.choice(responses["default"])
    return response

# Main loop to take user input and generate responses
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)
