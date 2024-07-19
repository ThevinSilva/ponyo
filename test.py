import RPi.GPIO as GPIO
import time

# Disable GPIO warnings
GPIO.setwarnings(False)

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the first motor
ENB = 4   # Physical pin 7
IN4 = 17  # Physical pin 11
IN3 = 27  # Physical pin 13

# Setup GPIO pins
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# Set PWM for speed control on ENB
pwmB = GPIO.PWM(ENB, 1500)  # Frequency in Hz
pwmB.start(0)  # Start PWM with 0% duty cycle (motor off)

def set_motor_speed(pwm, speed):
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0
    pwm.ChangeDutyCycle(speed)

def motor_forward(speed):
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    set_motor_speed(pwmB, speed)

def motor_backward(speed):
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    set_motor_speed(pwmB, speed)

try:
    while True:
        print("Motor forward at 50% speed")
        motor_forward(100)
        time.sleep(2)
        
        print("Motor forward at 100% speed")
        motor_forward(100)
        time.sleep(2)
        
        print("Motor backward at 50% speed")
        motor_backward(100)
        time.sleep(2)
        
        print("Motor backward at 100% speed")
        motor_backward(100)
        time.sleep(2)

except KeyboardInterrupt:
    pass

# Cleanup
pwmB.stop()
GPIO.cleanup()