from inspect import Attribute
import secrets
from cute import errors

def gen_salt(cfg):
	r = secrets.token_hex(32)
	setattr(cfg, "salt", r)
	return

def attr_check(cfg, attr : str):
	try:
		getattr(cfg, attr)
	except AttributeError:
		return getattr(errors.HashErrors, "HASHE_NO" + attr.upper())

	if len(getattr(cfg, attr)) == 0:
		print("HASHE_EMPTY" + attr.upper())
		return getattr(errors.HashErrors, "HASHE_EMPTY" + attr.upper())

	return 0
