from inspect import Attribute
import secrets, hashlib
from cute import errors

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

"""
def attr_check(cfg, attr : str):
	try:
		getattr(cfg, attr)
	except AttributeError:
		return getattr(errors.HashErrors, "HASHE_NO" + attr.upper())

	if len(getattr(cfg, attr)) == 0:
		print("HASHE_EMPTY" + attr.upper())
		return getattr(errors.HashErrors, "HASHE_EMPTY" + attr.upper())

	return 0
"""
