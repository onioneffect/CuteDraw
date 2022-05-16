import cute
import os, sys

from cute import flask_backend

# TODO: Separate config.json and crypto.json

def main(config):
	if not os.path.isdir(config.outdir):
		os.mkdir(config.outdir)

	ret = config.attr_check("salt")

	if ret != cute.errors.HashErrors.HASHE_SUCCESS:
		cute.crypto.gen_salt(config)
		cute.settings.save_config(config)

	cute.flask_backend.app.run("0.0.0.0")

	return 0

if __name__ == "__main__":

	client_settings = cute.settings.load_config()

	# Ay it works
	flask_backend.client_settings = client_settings

	try:
		main(client_settings)
	except KeyboardInterrupt:
		sys.exit(0)
