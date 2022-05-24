import secrets, hashlib

class SessionObj:
	unix_timestamp : int
	session_salt : int
	cookie : int

	def __init__(self, u, s, c):
		self.unix_timestamp = u
		self.session_salt = s
		self.cookie = c

def gen_salt(cfg):
	r = secrets.token_hex(32)
	setattr(cfg, "salt", r)
	return

def gen_hash(cfg, pass_word):
	h = hashlib.new("sha512")
	h.update(bytes(pass_word, "utf-8"))
	h.update(bytes.fromhex(cfg.salt))

	return h

def check_pass(cfg, pass_word):
	attempt = gen_hash(cfg, pass_word).hexdigest()
	expected = getattr(cfg, "hash")

	return attempt == expected

def gen_cookie(cfg, t):
	cfg.sessions = list()

	session_salt = secrets.token_hex(32)

	h = hashlib.new("sha512")
	h.update(t.to_bytes(8, byteorder="little"))
	h.update(bytes.fromhex(session_salt))
	h.update(bytes.fromhex(cfg.salt))

	current_sess = SessionObj(t, session_salt, h.hexdigest())
	cfg.sessions.append(current_sess.__dict__)

	return h
