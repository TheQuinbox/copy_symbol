import application
import sys

def setup():
	sys.dont_write_bytecode = True
	application.setup_logging()
	app = application.Application()
	app.logger.info(f"Starting {app.name} V{app.version}")
	app.run()

if __name__ == "__main__":
	setup()
