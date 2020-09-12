# coding: UTF-8
from picamera import PiCamera
import time
import pyocr as ocr
import pyocr.builders
from PIL import Image

def main():
    # カメラで撮影
    camera = PiCamera() 
    camera.resolution = (2592, 1944)

    img_path = '/home/pi/Documents/raspberrypi/single_function/test.png'

    camera.start_preview()
    time.sleep(10)
    camera.capture(img_path)
    camera.stop_preview()

    # OCRで文字列を取得
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]
    res = tool.image_to_string(Image.open(img_path), lang="eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6))
    print(res)

if __name__ == '__main__':
	main()
