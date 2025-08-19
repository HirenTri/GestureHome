import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import winsound

#beeping
freq=2000
dur=200

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ad91b6418c8049fe912bf872d6d865f1"

def speak(text):
    #engine.say("I will speak this text")
    engine.say(text)
    engine.runAndWait()
    
def processCommand(text):
    print(text)
    if "open google" in text.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in text.lower():
        webbrowser.open("https://www.facebook.com") 
    elif "open youtube" in text.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open insta" in text.lower():
        webbrowser.open("https://www.instagram.com")
        
    elif text.lower().startswith("play"):
        song = text.lower().split(" ")[1]
        # link = musiclibrary.music[song]
        # webbrowser.open(link)
        
    elif "news" in text.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            
            data = r.json()

            if 'articles' in data:
                articles = data['articles']
                
                print("Top Headlines:")
                speak("Top Headlines:")
                if articles:
                    for i, article in enumerate(articles, 1):
                        print(f"{i}. {article['title']}")
                        speak(article['title'])
                else:
                    print("No articles found.")
            else:
                print("'articles' key not found in the response.")
        else:
            print(f"Failed to fetch data. Status code: {r.status_code}")
            
           
def listen(channel):
    #speak("Listening......")
    
    with sr.Microphone() as src:
        print("Recognising...")
        winsound.Beep(freq, dur)
        
        try:
            audio = r.listen(src, phrase_time_limit=2)
            text = r.recognize_google(audio)
            
            processCommand(text)
            
            # Update channel if input is a number
            if text.isdigit():
                ch = int(text)
                if 0 < ch < 1000:
                    channel = ch  
                    webbrowser.open(f"http://127.0.0.1:5500/web_page/page{channel}.html")  
                
        except Exception as e:
            print("No input: {0}".format(e))
    
    return channel

        
if __name__ == "__main__":
    a = 0
    a = listen(a)
    print(a)