import cute
import logging, os

def main():
	logging.debug("Running Flask app")
	cute.flask_backend.app.run()

	return 0

if __name__ == "__main__":
	cute.log.init_log(logging.DEBUG)

	logging.debug("Calling %s" % cute.settings.load_config)
	client_settings = cute.settings.load_config()
	logging.debug("Returned %s with %d attributes" \
		 % (client_settings, len(dir(client_settings))))

	logging.debug("Calling %s" % main)
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)

