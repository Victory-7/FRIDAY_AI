import transformers

class FRIDAY_NLP:
    def __init__(self):
        self.model = transformers.pipeline("text-generation", model="gpt2")
    
    def process(self, user_input):
        """Processes user input and returns an AI-generated response."""
        try:
            response = self.model(user_input, max_length=150, do_sample=True)
            return response[0]["generated_text"].strip()
        except Exception as e:
            return f"Error: {str(e)}"
