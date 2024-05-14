import RPi.GPIO as GPIO
import time
# Pin Definitions
pwm_pin = 17  # PWM pin connected to an LED
direction_pin = 27  # Direction pin

# PWM Settings
frequency = 1000  # Frequency in Hz

# Set up the GPIO channel
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(direction_pin, GPIO.OUT)

# Initialize PWM on pwm_pin with frequency
pwm = GPIO.PWM(pwm_pin, frequency)

# Start PWM with 0% duty cycle
pwm.start(0)

try:
    while True:
        # Get user input for the duty cycle
        duty_cycle = input("Enter Duty Cycle (0-100) or 'exit' to quit: ")
        
        if duty_cycle.lower() == 'exit':
            break

        try:
            duty_cycle = float(duty_cycle)
            if 0 <= duty_cycle <= 100:
                pwm.ChangeDutyCycle(duty_cycle)
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        
        # Get user input for the direction
        direction = input("Enter Direction (0 or 1): ")
        
        try:
            direction = int(direction)
            if direction in [0, 1]:
                start = time.time()
                # Run the loop for 10 seconds
                while time.time() - start < 10:
                    GPIO.output(direction_pin, direction)
                    time.sleep(0.01)
            else:
                print("Please enter 0 or 1 for direction.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

except KeyboardInterrupt:
    pass

# Stop PWM
pwm.stop()

# Clean up GPIO
GPIO.cleanup()