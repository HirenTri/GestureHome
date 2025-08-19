from pyfirmata import Arduino, util
import time

# Setup board (Make sure you replace with the correct port of your Arduino)
board = Arduino('COM5')  # For Linux or Mac, or 'COMx' for Windows

# Initialize a PWM pin (e.g., pin 9)
pwm_pin = board.get_pin('d:9:p')  # d:9:p means digital pin 9 as PWM output

# Define max power for scaling
max_power = 100  # Adjust this to match the power scale you are using

# Simulating appliance data
appliance = {
    'name': "Fan",
    'status': "ON",  # Can be "ON" or "OFF"
    'power': 1 # Power value, should be between 0 and max_power
}

if appliance['name'] == "Fan":
    if appliance['status'] == "ON":
        # Scale appliance power (assumes power is between 0 and max_power)
        pwm_value = int(255 * appliance['power'] * appliance['power'] / max_power)  # Scale power to 0-255 range
        pwm_pin.write(pwm_value / 255.0)  # PyFirmata requires a float value (0.0 to 1.0)
        print(f"Fan is ON, PWM Value: {pwm_value}")
    else:
        pwm_pin.write(0)  # Turn off the fan (set PWM to 0)
        print("Fan is OFF")

# Keep the board active

time.sleep(5)
