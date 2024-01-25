from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

# Load pre-trained DistilBERT model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# chatbot function with input validation
def chatbot_response(user_input):
    # Tokenize and process user input
    inputs = tokenizer(user_input, return_tensors='pt', truncation=True, padding=True)
    
    # Forward pass through the model
    outputs = model(**inputs)
    
    # Dummy logic for illustrative purposes
    if outputs.logits[0][1] > outputs.logits[0][0]:
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
