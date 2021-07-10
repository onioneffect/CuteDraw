import logging

fmt = "[%(asctime)s] %(message)s"
date_format = "%Y-%m-%d %I:%M:%S %p"

def init_log(mode : int = logging.INFO):
	logging.basicConfig(level=mode, format=fmt, datefmt=date_format)
	return 1

