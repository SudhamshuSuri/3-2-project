import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# Define the motor pins
motorPins = [18, 23, 24, 25]

# Define the direction pins
directionPins = [17, 27]

# Set up the motor pins as output pins
for pin in motorPins:
    GPIO.setup(pin, GPIO.OUT)

# Set up the direction pins as output pins
for pin in directionPins:
    GPIO.setup(pin, GPIO.OUT)

# Define the function to set the direction of the motor
def set_direction(pin, direction):
    if direction == "forward":
        GPIO.output(pin, GPIO.HIGH)
    elif direction == "reverse":
        GPIO.output(pin, GPIO.LOW)
    else:
        raise ValueError("Invalid direction")

# Define the function to set the speed of the motor
def set_speed(speed):
    if speed < 0 or speed > 100:
        raise ValueError("Invalid speed")
    duty_cycle = int(abs(speed) * 10.23)  # Convert speed to duty cycle
    if speed < 0:
        for pin in motorPins:
            GPIO.output(pin, GPIO.LOW)
        for pin in directionPins:
            set_direction(pin, GPIO.LOW)
    else:
        for pin in directionPins:
            set_direction(pin, GPIO.HIGH)
    GPIO.output(motorPins[0], GPIO.HIGH)
    GPIO.output(motorPins[1], GPIO.LOW)
    GPIO.output(motorPins[2], GPIO.HIGH)
    GPIO.output(motorPins[3], GPIO.LOW)
    pwm = GPIO.PWM(motorPins[0], 100)
    pwm.start(duty_cycle)
    pwm.ChangeDutyCycle(duty_cycle)

# Define the function to stop the motor
def stop_motor():
    for pin in motorPins:
        GPIO.output(pin, GPIO.LOW)
    for pin in directionPins:
        set_direction(pin, GPIO.LOW)

# Set the direction of the motor to forward
for pin in directionPins:
    set_direction(pin, GPIO.HIGH)

# Set the speed of the motor to 50%
set_speed(50)

# Wait for 5 seconds
time.sleep(5)

# Stop the motor
stop_motor()

# Clean up the GPIO pins
GPIO.cleanup()