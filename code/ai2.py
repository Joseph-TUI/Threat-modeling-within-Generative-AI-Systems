class GenerativeAIModel:
    def generate_response(self, user_input):
        # Assume a Generative AI model that concatenates user input
        # This is just a placeholder and not a realistic Generative AI model
        generated_output = "Generative AI Response: " + user_input
        return generated_output

# Instantiate the Generative AI model
generative_model = GenerativeAIModel()

# User input
user_input = "How does the algorithm work?"

# Generate a response using the original user input
original_output = generative_model.generate_response(user_input)
print("Original Output:", original_output)

# Attack: Spoofing the input to manipulate the output
spoofed_input = "Malicious input designed to deceive the model"
spoofed_output = generative_model.generate_response(spoofed_input)
print("Spoofed Output:", spoofed_output)
