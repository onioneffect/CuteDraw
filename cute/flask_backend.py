import random, os
from cute import images
from flask import Flask, send_file, request

def random_pic(s : str):
	f = random.choice(os.listdir(s))
	return os.path.join(s, f)

app = Flask("CuteDraw")

@app.route('/get_image')
def get_image():
	rget = request.args.get

	if not (rget("claim") and rget("user")):
		return send_file("img/donda.png")
	else:
		s = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		return send_file(images.generate_img("img/sup.jpg", s))
