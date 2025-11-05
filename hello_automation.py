# hello_automation.py
import datetime

def greet_user():
    """Simple greeting based on time of day"""
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    name = input("What's your name? ")
    print(f"{greeting}, {name}! Welcome to AI & Automation Engineering!")
    print(f"Today is {datetime.datetime.now().strftime('%B %d, %Y')}")

if __name__ == "__main__":
    greet_user()
    
