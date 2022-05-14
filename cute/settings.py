import cute.errors
import logging, json, os, sys

class Settings:
	def __init__(self, j : dict):
		for k in j.keys():
			setattr(self, k, j[k])

def cfg_path_check():
	try:
		return sys.argv[1]
	except IndexError:
		return "config.json"

def load_config():
	cfg_path = cfg_path_check()

	logging.debug("Opening config file %s" %cfg_path)
	try:
		fp = open(cfg_path)
	except FileNotFoundError:
		logging.critical(cute.errors.CFG_NOTFOUND %cfg_path)
		sys.exit(1)

	if os.stat(cfg_path).st_size == 0:
		logging.critical(cute.errors.CFG_EMPTY %cfg_path)
		sys.exit(2)

	logging.debug("Running json.load on config file")
	json_content = json.load(fp)
	fp.close()

	return Settings(json_content)

def save_config(cfg):
	cfg_path = cfg_path_check()

	try:
		fp = open(cfg_path, "w")
	except FileNotFoundError:
		logging.critical(cute.errors.CFG_NOTFOUND %cfg_path)
		sys.exit(1)

	json_saveme = json.dumps(cfg.__dict__)
	fp.write(json_saveme)
	fp.close()

	return
