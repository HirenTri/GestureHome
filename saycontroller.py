import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties like rate and volume (optional)
engine.setProperty('rate', 100)  # Speed of speech (words per minute)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Say "on"
engine.say("on")
engine.runAndWait()

# Say "off"
engine.say("off")
#engine.runAndWait()
