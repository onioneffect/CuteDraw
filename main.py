import cute
import logging, os, sys

from cute import flask_backend

def main(config):
	logging.debug("Checking if outdir `%s` exists...", config.outdir)
	if not os.path.isdir(config.outdir):
		logging.debug("Does not exist! Creating new one...")
		os.mkdir(config.outdir)
	else:
		logging.debug("Already exists!")

	# Generate salt while setting up the program because it's random anyways
	logging.debug("Calling %s with `salt`...", config.attr_check)
	ret = config.attr_check("salt")
	logging.debug(cute.errors.HashErrors.m[ret])

	if ret != cute.errors.HashErrors.HASHE_SUCCESS:
		cute.crypto.gen_salt(config)

		logging.debug("Saving config...")
		cute.settings.save_config(config)

	logging.debug("Calling %s" % cute.flask_backend.app.run)
	cute.flask_backend.app.run("0.0.0.0")

	return 0

if __name__ == "__main__":
	cute.log.init_log(logging.DEBUG)

	logging.debug("Calling %s" % cute.settings.load_config)
	client_settings = cute.settings.load_config()
	logging.debug("Returned %s with %d attributes" \
		% (client_settings, len(dir(client_settings)))
	)

	# Ay it works
	flask_backend.client_settings = client_settings

	logging.debug("Calling %s with %s" % (main, client_settings))
	try:
		main(client_settings)
	except KeyboardInterrupt:
		sys.exit(0)
