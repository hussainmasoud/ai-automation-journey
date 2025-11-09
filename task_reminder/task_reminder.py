import schedule
import time
import pyttsx3
from datetime import datetime

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

tasks = []

def add_task(task, reminder_time):
    tasks.append((task, reminder_time))
    schedule.every().day.at(reminder_time).do(remind, task=task)
    print(f"✅ Task added: '{task}' at {reminder_time}")

def remind(task):
    message = f"Reminder! It's time to: {task}"
    print(message)
    speak(message)

def main():
    print("AI Task Reminder Bot")
    print("Type your tasks like: Clean room at 14:30")
    print("Type 'done' when finished.\n")

    while True:
        user_input = input("Enter task & time: ")

        if user_input.lower() == "done":
            break

        # Example input: "Pray Dhuhr at 13:10"
        if " at " in user_input:
            task, time_str = user_input.split(" at ")
            add_task(task, time_str)
        else:
            print("❗ Format example: Study AI at 20:00")

    print("\n⏳ Reminders started... keep this window open.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
