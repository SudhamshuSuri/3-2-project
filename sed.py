import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the motor pins
motorPin1 = 17
motorPin2 = 22
enablePin = 23

# Set up the motor pins as output pins
GPIO.setup(motorPin1, GPIO.OUT)
GPIO.setup(motorPin2, GPIO.OUT)
GPIO.setup(enablePin, GPIO.OUT)

# Define the function to set the direction of the motor
def set_direction(direction):
    if direction == 0:
        # Stop the motor
        GPIO.output(enablePin, GPIO.LOW)
    elif direction == 1:
        # Move the motor forward
        GPIO.output(motorPin1, GPIO.HIGH)
        GPIO.output(motorPin2, GPIO.HIGH)
        GPIO.output(enablePin, GPIO.HIGH)
    elif direction == 2:
        # Move the motor backward
        GPIO.output(motorPin1, GPIO.LOW)
        GPIO.output(motorPin2, GPIO.LOW)
        GPIO.output(enablePin, GPIO.HIGH)
    else:
        raise ValueError("Invalid direction")

# Test the function
set_direction(1)  # Move the motor forward
time.sleep(2)
set_direction(2)  # Move the motor backward
time.sleep(2)
set_direction(0)  # Stop the motor

# Clean up the GPIO pins
GPIO.cleanup()