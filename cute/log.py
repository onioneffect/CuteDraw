import logging

def init_log(mode : int = logging.INFO):
	logging.basicConfig(
		level=mode,
		format="[%(asctime)s] %(message)s",
		datefmt="%Y-%m-%d %I:%M:%S %p"
	)

	return 1

