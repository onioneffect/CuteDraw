import hashlib, os
from PIL import Image, ImageFont, ImageDraw

def generate_img(path : str, text : str):
	out_filename = hashlib.md5(text.encode("ascii")).hexdigest()
	out_path = "output/" + out_filename + ".jpg"

	if os.path.exists(out_path):
		return out_path

	# else:
	x, y = 460, 690
	w, h = 90, 40
	shape = [(x, y), (x + w, y + h)]

	image = Image.open(path)

	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(r'cute/TTF/wild.ttf', 18)

	draw.rectangle(shape, fill = "black")
	draw.text((x, y), text, fill = "white", font = font, align ="left")

	image.save(out_path)
	return out_path
