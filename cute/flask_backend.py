import cute
from flask import Flask, send_file, request

app = Flask("CuteDraw")
client_settings : cute.settings.Settings

@app.route("/fantasy")
def admin():
	hash_code = cute.crypto.attr_check(client_settings, "hash")

	if hash_code in (3, 4):
		return "Create your password please: "
	else:
		return "Enter your password: "

@app.route("/get_image")
def get_image():
	rget = request.args.get

	if not (rget("claim") and rget("user")):
		return send_file("img/donda.png")
	else:
		s = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		return send_file(cute.images.generate_img("img/sup.jpg", s))
