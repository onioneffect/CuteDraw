import cute
from flask import Flask, send_file, request, render_template

app = Flask("CuteDraw")
client_settings : cute.settings.Settings

@app.route("/fantasy", methods = ['POST', 'GET'])
def admin():
	hash_code = cute.crypto.attr_check(client_settings, "hash")
	pass_created = hash_code not in (3, 4)

	if request.method == 'POST':
		# pw = request.form['AF']
		debug = "Posting..."
	else:
		debug = "Getting..."

	return render_template(
		"fantasy.html",
		username = debug,
		created = pass_created
	)

@app.route("/get_image")
def get_image():
	rget = request.args.get

	if not (rget("claim") and rget("user")):
		pass
	else:
		s = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		return send_file(cute.images.generate_img("cute/img/sup.jpg", s))
