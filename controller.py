import pyfirmata

comport='COM5'

board = pyfirmata.Arduino(comport)

led_00=board.get_pin('d:6:o')
led_01=board.get_pin('d:7:o')

led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:p')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')
led_6=board.get_pin('d:5:o')
    
# appliances = [
#     {"name": "Light", "status": "OFF"},
#     {"name": "Fan", "status": "OFF"},
#     {"name": "AC", "status": "OFF"},
#     {"name": "TV", "status": "OFF"},
#     {"name": "Geyser", "status": "OFF"}
# ]

def switch(on):
    if on == True: 
        led_00.write(0)
        led_01.write(1)
    else:
        led_00.write(1)
        led_01.write(0)

def led(appliances):
    for appliance in appliances:
        if appliance['name'] == "Light":
            if appliance['status'] == "ON":
                led_1.write(1)
            else:
                led_1.write(0)
                
        if appliance['name'] == "Fan":
            if appliance['status'] == "ON":
                max_power = 100
                pwm_value = int(255 * appliance['power'] * appliance['power'] * 2 / max_power)  # Scale power to 0-255 range
                led_2.write(pwm_value / 255.0) 
            else:
                led_2.write(0)
                
        if appliance['name'] == "AC":
            if appliance['status'] == "ON":
                led_3.write(1)
            else:
                led_3.write(0)
                
        if appliance['name'] == "TV":
            if appliance['status'] == "ON":
                led_4.write(1)
            else:
                led_4.write(0)
                
        if appliance['name'] == "Geyser":
            if appliance['status'] == "ON":
                led_5.write(1)
            else:
                led_5.write(0)
                
        if appliance['name'] == "Speaker":
            if appliance['status'] == "ON":
                led_6.write(1)
            else:
                led_6.write(0)
    
        
