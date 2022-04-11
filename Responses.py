from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ("hello", "hi", "wassup"):
        return "Hi! Welcome to Hyphae!"
    if user_message in ("next round"):
        now = datetime.now()
        date_time = now.strftime("%H:%M:%S")
        return str(date_time)
        
    return "I don't understand you."

