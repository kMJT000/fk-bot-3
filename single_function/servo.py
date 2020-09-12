import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
servo = GPIO.PWM(17,50)

servo.start(7.25)
time.sleep(2)

servo.start(2.5)
time.sleep(2)

servo.start(7.25)
time.sleep(2)

servo.start(12)
time.sleep(2)

servo.stop()
GPIO.cleanup()
