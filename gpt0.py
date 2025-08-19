import time

for i in range(1, 6):
    print(f'\r{i}', end='')  # Use '\r' to return to the beginning of the line
    time.sleep(2)  # Pause for 1 second to simulate step-by-step output
