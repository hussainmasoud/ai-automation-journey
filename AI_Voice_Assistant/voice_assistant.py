import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "assistant" in command:
                command = command.replace("assistant", "")
                print("Command:", command)
    except:
        command = ""
    return command

def run_assistant():
    command = listen_command()
    print(command)

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + time)

    elif "open youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "send message" in command:
        talk("Who do you want to message?")
        # Example: send WhatsApp message (customize this later)
        pywhatkit.sendwhatmsg("+255XXXXXXXXX", "Hello from your AI assistant!", 15, 0)

    elif "stop" in command or "exit" in command:
        talk("Goodbye, see you soon!")
        exit()

    else:
        talk("Please say the command again.")

while True:
    run_assistant()
