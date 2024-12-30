import logging

from src.domain.utilities.settings import SETTINGS

# Inspired by https://medium.com/@emanueleorecchio/crafting-your-custom-logger-in-python-a-step-by-step-guide-0824bfd9b939


class CustomFormatter(logging.Formatter):
	grey = "\x1b[37;1m"
	yellow = "\x1b[33;20m"
	red = "\x1b[31;20m"
	bold_red = "\x1b[31;1m"
	green = "\x1b[1;32m"
	reset = "\x1b[0m"
	format: str = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
	# TODO datefmt should be here

	FORMATS = {
		logging.DEBUG: grey + format + reset,
		logging.INFO: green + format + reset,
		logging.WARNING: yellow + format + reset,
		logging.ERROR: red + format + reset,
		logging.CRITICAL: bold_red + format + reset,
	}

	def format(self, record):
		log_fmt = self.FORMATS.get(record.levelno)
		formatter = logging.Formatter(fmt=log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
		return formatter.format(record)


class Logger(logging.Logger):
	""" """

	def __init__(self, name, level=logging.NOTSET):
		super().__init__(name, level)
		self.extra_info = None

		# Add handlers (e.g., ConsoleHandler, FileHandler, etc.)
		handler = logging.StreamHandler()
		handler.setFormatter(fmt=CustomFormatter())
		self.addHandler(handler)


match SETTINGS.LOG_LEVEL:
	case "debug":
		log_level = logging.DEBUG
	case "info":
		log_level = logging.INFO
	case "warning":
		log_level = logging.WARNING
	case "error":
		log_level = logging.ERROR
	case _:
		log_level = logging.INFO

logger = Logger(name="python-api-template", level=log_level)
