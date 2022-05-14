import os
import hashlib
from PIL import Image, ImageFont, ImageDraw

def generate_img(path : str, text : str):
	w, h = 90, 40
	shape = [(450, 690), (450 + w, 690 + h)]

	image = Image.open(path)

	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(r'wild.ttf', 18)

	draw.rectangle(shape, fill = "black")
	draw.text((420, 700), text, fill = "white", font = font, align ="left")

	out_filename = hashlib.md5(text.encode("ascii")).hexdigest()
	out_path = "output/" + out_filename + ".jpg"

	image.save(out_path)
	return out_path

if __name__ == "__main__":
	import sys
	generate_img(sys.argv[1], sys.argv[2])
