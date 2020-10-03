import RPi.GPIO as GPIO
import time

Led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_pin, GPIO.OUT)

GPIO.output(Led_pin, GPIO.HIGH)
time.sleep(5)
GPIO.output(Led_pin, GPIO.LOW)

GPIO.cleanup()