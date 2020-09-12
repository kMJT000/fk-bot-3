# coding: UTF-8
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import pyocr as ocr
import pyocr.builders
from PIL import Image

def main():
    img_path = '/home/pi/Documents/raspberrypi/single_function/test.png'

    servo_move()
    photo(img_path)
    photo_recognition(img_path)

def servo_move():
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

 # カメラで撮影
def photo(img_path):
    camera = PiCamera() 
    camera.resolution = (2592, 1944)

    camera.start_preview()
    time.sleep(10)
    camera.capture(img_path)
    camera.stop_preview()

 # OCRで文字列を取得
def photo_recognition(img_path):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    res = tool.image_to_string(Image.open(img_path), lang="eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    print(res)

if __name__ == '__main__':
	main()
