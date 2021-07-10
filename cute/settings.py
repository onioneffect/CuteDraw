import cute.errors, cute.log
import logging, json, os, sys

class Settings:
	def __init__(self, j : dict):
		for k in j.keys():
			setattr(self, k, j[k])

def load_config():
	try:
		cfg_path = sys.argv[1]
	except IndexError:
		cfg_path = "config.json"

	logging.debug("Opening config file %s" %cfg_path)
	try:
		fp = open(cfg_path)
	except FileNotFoundError:
		logging.critical(errors.CFG_NOTFOUND %cfg_path)
		sys.exit(1)

	if os.stat(cfg_path).st_size == 0:
		logging.critical(errors.CFG_EMPTY %cfg_path)
		sys.exit(2)

	logging.debug("Running json.load on config file")
	json_content = json.load(fp)
	
	return Settings(json_content)

