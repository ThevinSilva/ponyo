import RPi.GPIO as GPIO
import time

# Motors are being driven by 5 PCS L298N Motor Drive Controller Board Module Dual H Bridge DC
class Controller:

    def __init__(self, frequency=1500, speed = 80):
        self.speed = speed
        self.pins = {
            "ENA": 23,
            "IN1": 24,
            "IN2": 25,
            "IN3": 27,
            "IN4": 22,
            "ENB": 4
        }
        GPIO.setmode(GPIO.BCM)
        [GPIO.setup(pin, GPIO.OUT) for pin in self.pins.values()]
        self.pwmA = GPIO.PWM(self.pins["ENA"], frequency)  # Frequency in Hz
        self.pwmB = GPIO.PWM(self.pins["ENB"], frequency)  # Frequency in Hz
        self.pwmA.start(0)
        self.pwmB.start(0)

    def set_motor_speed(self, pwm):
        pwm.ChangeDutyCycle(self.speed)

    def tail_up(self):
        GPIO.output(self.pins["IN4"], GPIO.HIGH)
        GPIO.output(self.pins["IN3"], GPIO.LOW)
        self.set_motor_speed(self.pwmB)

    def tail_down(self):
        GPIO.output(self.pins["IN4"], GPIO.LOW)
        GPIO.output(self.pins["IN3"], GPIO.LOW)
        self.set_motor_speed(self.pwmB)

    def head_up(self):
        GPIO.output(self.pins["IN3"], GPIO.HIGH)
        GPIO.output(self.pins["IN4"], GPIO.LOW)
        self.set_motor_speed(self.pwmB)


    def head_down(self):
        GPIO.output(self.pins["IN3"], GPIO.LOW)
        GPIO.output(self.pins["IN4"], GPIO.LOW)
        self.set_motor_speed(self.pwmB)

    def mouth_close(self):
        GPIO.output(self.pins["IN1"], GPIO.HIGH)
        GPIO.output(self.pins["IN2"], GPIO.LOW)
        self.set_motor_speed(self.pwmA)


    def mouth_open(self):
        GPIO.output(self.pins["IN1"], GPIO.LOW)
        GPIO.output(self.pins["IN2"], GPIO.HIGH)
        self.set_motor_speed(self.pwmA)

    # Cleanup
    def __del__(self):
        self.pwmA.stop()
        self.pwmB.stop()
        GPIO.cleanup()

if __name__ == "__main__":

    try:
        c = Controller(200)

        while True:

            # Full Articulation Demo
            # c.head_up()
            # time.sleep(1)
            # c.head_down()
            # time.sleep(1)
            # c.tail_up()
            # time.sleep(1)
            # c.tail_down()
            # time.sleep(1)
            # c.mouth_open()
            # time.sleep(1)
            # c.mouth_close()
            # time.sleep(1)

            # talk demo
            c.mouth_open()
            time.sleep(0.1)
            c.mouth_close()
            time.sleep(0.1)

    except KeyboardInterrupt:   
        del c
