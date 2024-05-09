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

def steer(angle):
    # Convert angle (0-180) to duty cycle (2-12)
    duty_cycle = (angle / 18) + 2
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  # Adjust this delay as needed for your servo motor


while True:
    # Prompt user for input
    direction = input("Enter 'l' to turn left or 'r' to turn right: ")

    # Turn left
    if direction == 'l':
        steer(90)
    
    print(f'we turned this way {direction}')

    # Turn right
    if direction == 'r':
        steer(-90)   # Set servo angle to 0 degrees (right)
    
    else:
        print("Invalid input. Please enter 'l' to turn left or 'r' to turn right.")
        continue
