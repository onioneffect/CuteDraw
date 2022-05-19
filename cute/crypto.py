import datetime
import secrets, hashlib

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

def gen_cookie(cfg, pass_word, t):
	setattr(cfg, "logged", t)

	h = hashlib.new("sha512")
	h.update(t.to_bytes(8, byteorder="little"))
	h.update(bytes(pass_word, "utf-8"))
	h.update(bytes.fromhex(cfg.salt))

	return h
