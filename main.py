import cute
import logging, os, sys

def main(config):
	logging.debug("Checking if outdir `%s` exists...", config.outdir)
	if not os.path.isdir(config.outdir):
		logging.debug("Does not exist! Creating new one...")
		os.mkdir(config.outdir)
	else:
		logging.debug("Already exists!")

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

	logging.debug("Calling %s with %s" % (main, client_settings))
	try:
		main(client_settings)
	except KeyboardInterrupt:
		sys.exit(0)
