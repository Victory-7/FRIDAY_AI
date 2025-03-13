import speech_recognition as sr
import pyttsx3

class FRIDAY_Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
    
    def speak(self, text):
        """Converts text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listens for user voice input and converts it to text."""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return ""
            except sr.RequestError:
                print("Could not request results. Check your internet connection.")
                return ""
