import threading
from nlp_engine import FRIDAY_NLP
from self_coding import FRIDAY_Coder
from voice_assistant import FRIDAY_Voice

def main():
    print("FRIDAY AI is starting...")
    
    # Initialize modules
    nlp = FRIDAY_NLP()
    coder = FRIDAY_Coder()
    voice = FRIDAY_Voice()
    
    # Start voice assistant in a separate thread
    voice_thread = threading.Thread(target=voice.listen)
    voice_thread.start()
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Shutting down FRIDAY AI...")
            break
        
        response = nlp.process(user_input)
        print("FRIDAY:", response)
        
        # If user asks FRIDAY to code something
        if "code" in user_input.lower():
            generated_code = coder.generate_code(user_input)
            print("Generated Code:\n", generated_code)
    
    voice_thread.join()
    
if __name__ == "__main__":
    main()
