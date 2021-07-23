import random, os
from flask import Flask, send_file, request

def random_pic(s : str):
	f = random.choice(os.listdir(s))
	return os.path.join(s, f)

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
		print(request.remote_addr)
		return send_file(random_pic("img"))

