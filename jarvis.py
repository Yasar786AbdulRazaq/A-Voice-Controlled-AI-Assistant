import os
from dotenv import load_dotenv
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import requests

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print("Assistant:", audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}")
    except Exception:
        print("Say that again please...")
        return None
    return query

def greet():
    speak("Hello my friend Yasar Bhai, how can I help you today?")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('youremail@gmail.com', 'yourpassword')  # ⚠️ Use secure method in real projects
        server.sendmail('youremail@gmail.com', to, content)
        server.quit()
        speak("Email has been sent!")
    except Exception as e:
        speak("Unable to send email.")
        print(e)

def get_ai_response(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(url, params=params, headers=headers, json=data)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Sorry, I couldn't reach the AI service."
    except Exception as e:
        print("Error:", e)
        return "There was an error contacting the AI service."

def open_email():
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/yasarabdulrazaq/")

def open_github():
    webbrowser.open("https://github.com/Yasar786AbdulRazaq")

# ========== Main Program ==========
if __name__ == '__main__':
    greet()
    while True:
        query = takecommand()
        if query is None:
            continue

        query = query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open my google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open my youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open my email' in query:
            open_email()

        elif 'open my linkedin' in query:
            open_linkedin()

        elif 'open my github' in query:
            open_github()

        elif 'how are you' in query:
            speak("I am fine Yasar, my friend. How can I help you?")

        elif 'hi jarvis' in query:
            speak("Hello Yasar Bhai! Please ask your question.")

        elif 'open notepad' in query:
            os.system("start notepad")

        elif 'open calculator' in query:
            os.system("start calc")

        elif 'what time is it now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'send email' in query:
            try:
                speak("What should I say in the email?")
                content = takecommand()
                to = "recipient@example.com"
                sendEmail(to, content)
            except:
                speak("Sorry, I couldn't send the email.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        else:
            speak("Let me think...")
            reply = get_ai_response(query)
            speak(reply)
