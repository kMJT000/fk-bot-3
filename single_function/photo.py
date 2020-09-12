from picamera import PiCamera
import time

camera = PiCamera() 
camera.resolution = (2592, 1944)

camera.start_preview()
time.sleep(10)
camera.capture('/home/pi/Documents/raspberrypi/single_function/test.jpg')
camera.stop_preview()
