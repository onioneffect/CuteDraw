import random, os
from flask import Flask, send_file, request

app = Flask("CuteDraw")

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/get_image')
def get_image():
	rget = request.args.get
	if not (rget("claim") and rget("user")):
		return "Error! :("
	else:
		return send_file("gently.png")

