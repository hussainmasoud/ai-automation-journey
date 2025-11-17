import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message["content"]
    return answer

def run_ai_assistant():
    speak("Hello Hussain, I'm your AI-powered assistant. How can I help you today?")

    while True:
        command = listen()

        if "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye! Talk to you later.")
            break

        # Send the user's voice command to ChatGPT
        ai_reply = ask_openai(command)

        # Speak the response
        speak(ai_reply)

run_ai_assistant()
