import cute, datetime
from flask import *

app = Flask("CuteDraw")
client_settings : cute.settings.Settings

def admin_redirect():
	now = datetime.datetime.now()
	t = int(now.timestamp())
	cookie_hash = cute.crypto.gen_cookie(client_settings, t)
	cute.settings.save_config(client_settings)

	r = make_response(render_template("dogs.html"))
	r.set_cookie(
		"auth", # key
		cookie_hash.hexdigest(), # value
		datetime.timedelta(hours=1) # max age
	)
	return r

def cookie_check(req) -> bool:
	cookie = req.cookies.get("auth")
	for dict in client_settings.sessions:
		if dict["cookie"] == cookie:
			return True

	return False

@app.route("/fantasy", methods = ['POST', 'GET'])
def prompt():
	if cookie_check(request):
		return admin_redirect()

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
				return admin_redirect()

	return render_template(
		"fantasy.html",
		created = pass_created
	)

@app.route("/get_image")
def get_image():
	rget = request.args.get

	if not (rget("claim") and rget("user")):
		return send_file(cute.images.generate_img("cute/img/sup.jpg", "Invalid"))
	else:
		s = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		return send_file(cute.images.generate_img("cute/img/sup.jpg", s))
