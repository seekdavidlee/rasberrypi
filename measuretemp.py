from gpiozero import CPUTemperature
from time import sleep

def monitor_temperature(interval=5, duration=None):
    cpu = CPUTemperature()

    if duration is not None:
        iterations = duration // interval
    else:
        iterations = float('inf')  # Run indefinitely

    try:
        while iterations > 0:
            temperature = cpu.temperature
            print(f"CPU Temperature: {temperature:.2f} °C")
            sleep(interval)
            iterations -= 1
    except KeyboardInterrupt:
        pass

# Call the function to monitor the temperature every 5 seconds indefinitely
monitor_temperature(interval=5)
