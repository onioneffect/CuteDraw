import cute
from flask import Flask, send_file, request, render_template

app = Flask("CuteDraw")
client_settings : cute.settings.Settings

@app.route("/fantasy", methods = ['POST', 'GET'])
def admin():
	hash_code = client_settings.attr_check("hash")
	pass_created = hash_code not in (3, 4)

	if request.method == 'POST':
		pw = request.form['AF']
		if pw and not pass_created:
			sha_obj = cute.crypto.gen_hash(client_settings, pw)
			setattr(client_settings, "hash", sha_obj.hexdigest())
			cute.settings.save_config(client_settings)
		elif pass_created:
			correct = cute.crypto.check_pass(client_settings, pw)
			if correct:
				print("Correct!")
			else:
				print("Wrong pass!")

	return render_template(
		"fantasy.html",
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
