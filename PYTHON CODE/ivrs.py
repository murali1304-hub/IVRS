import pyttsx3, speech_recognition as sr, webbrowser, os, pyjokes
from colorama import init, Fore

init(autoreset=True)
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print(Fore.CYAN + f"IVRS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        speak("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(Fore.GREEN + f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

def perform_task(command):
    if "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "play song" in command:
        speak("Playing your song...")
        os.system("start wmplayer")
    elif "joke" in command:
        speak(pyjokes.get_joke())
    elif "calculator" in command:
        speak("Opening calculator...")
        os.system("calc")
    else:
        speak("Command not recognized. Try again.")

def banner():
    print(Fore.YELLOW + """
    ██████╗ ██╗   ██╗██████╗ ███████╗
    ██╔══██╗██║   ██║██╔══██╗██╔════╝
    ██████╔╝██║   ██║██████╔╝█████╗  
    ██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  
    ██║     ╚██████╔╝██║     ███████╗
    ╚═╝      ╚═════╝ ╚═╝     ╚══════╝
    """)
    speak("Welcome to your voice assistant.")

if __name__ == "__main__":
    banner()
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            perform_task(command)
