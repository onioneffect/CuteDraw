import random, os
from cute import images, crypto
from flask import Flask, send_file, request

app = Flask("CuteDraw")

@app.route("/fantasy")
def admin():
	pass

@app.route("/get_image")
def get_image():
	rget = request.args.get

	if not (rget("claim") and rget("user")):
		return send_file("img/donda.png")
	else:
		s = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		return send_file(images.generate_img("img/sup.jpg", s))
