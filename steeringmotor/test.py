import RPi.GPIO as GPIO
import time

# Define servo pin
servo_pin = 17  # PWM pin for servo motor

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set servo pin as output
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM instance
servo_pwm = GPIO.PWM(servo_pin, 50)  # Frequency = 50Hz (standard for servo motors)

# Start PWM
servo_pwm.start(0)