import re
import random

class FRIDAY_Coder:
    def __init__(self):
        self.templates = {
            "python": [
                "def {function_name}():\n    # TODO: Implement function\n    pass",
                "class {class_name}:\n    def __init__(self):\n        pass"
            ],
            "c": [
                "#include <stdio.h>\nvoid {function_name}() {\n    // TODO: Implement function\n}"],
            "java": [
                "public class {class_name} {\n    public {class_name}() {\n        // Constructor\n    }\n}"],
        }
    
    def generate_code(self, request):
        """Generates simple boilerplate code based on user request."""
        try:
            if "python" in request.lower():
                template = random.choice(self.templates["python"])
                return template.format(function_name="my_function", class_name="MyClass")
            elif "c" in request.lower():
                template = random.choice(self.templates["c"])
                return template.format(function_name="myFunction")
            elif "java" in request.lower():
                template = random.choice(self.templates["java"])
                return template.format(class_name="MyClass")
            else:
                return "Sorry, I can't generate that language yet."
        except Exception as e:
            return f"Error: {str(e)}"
