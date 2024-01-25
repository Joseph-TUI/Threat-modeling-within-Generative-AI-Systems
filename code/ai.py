import spacy

# Load a pre-trained English NLP model
nlp = spacy.load("en_core_web_sm")

# chatbot function
def chatbot_response(user_input):
    doc = nlp(user_input)

    # Dummy logic for illustrative purposes
    if "return" in [token.text.lower() for token in doc]:
        return "Certainly! We have a return policy in place. Please visit our website for more details."
    else:
        return "I'm sorry, I didn't understand your question."

# Normal user interaction
user_input_normal = "How do I return a defective product?"
response_normal = chatbot_response(user_input_normal)
print("Normal User Interaction:", response_normal)

# Adversarial attack
user_input_adversarial = "I want to return a defective product by fixing it. Can you help me?"
response_adversarial = chatbot_response(user_input_adversarial)
print("Adversarial Attack:", response_adversarial)
