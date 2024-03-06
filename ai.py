import speech_recognition as sr
import pyttsx3

def get_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am advanced A.I. How can I assist you today?")

    while True:
        user_input = get_audio().lower()

        if "jarvis" in user_input:
            if "hello" in user_input:
                speak("Hello! How can I help you?")
            elif "goodbye" in user_input:
                speak("Goodbye")
                break
            else:
                speak("I am still learning. Please provide more instructions.")
        else:
            speak("I'm sorry, I only respond to commands when you mention my name.")