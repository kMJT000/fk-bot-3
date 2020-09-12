# coding: UTF-8
import pyocr as ocr
import pyocr.builders
from PIL import Image

def main():
	img_path = "sample.png"

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
    