import winsound

# Frequency of the sound (in Hz) and duration (in milliseconds)
frequency = 1100  # Frequency in Hz (higher values give higher pitch)
duration = 200     # Duration in milliseconds (100 ms for a short "tick")

# Play the sound
winsound.Beep(frequency, duration)
