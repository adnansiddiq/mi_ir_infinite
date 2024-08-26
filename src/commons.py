"""Logger settings"""
# Standard imports
from logging.handlers import RotatingFileHandler
import logging
import datetime as dt

# Paths
DIR_LOGS = "./"

# Logging
LOGGER_NAME = "log"
LOG_LEVEL = "DEBUG"
LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "notset": logging.NOTSET,
}


def logger(name=LOGGER_NAME):
    """Return logger of given name, without initialize it.

    Equivalent of logging.getLogger() call.
    """
    logger_obj = logging.getLogger(name)
    fmt_str = "%(levelname)s: [%(filename)s:%(lineno)s:%(funcName)s()] %(message)s"
    logging.basicConfig(format=fmt_str)
    return logger_obj


def log_level(level):
    """Set terminal/file log level to given one.
    .. note:: Don't forget the propagation system of messages:
        From logger to handlers. Handlers receive log messages only if
        the main logger doesn't filter them.
    """
    # Main logger
    _logger.setLevel(level.upper())
    # Handlers
    [
        handler.setLevel(level.upper())
        for handler in _logger.handlers
        if handler.__class__
        in (logging.StreamHandler, logging.handlers.RotatingFileHandler)
    ]


_logger = logging.getLogger(LOGGER_NAME)
_logger.setLevel(LOG_LEVEL)

# log file
formatter = logging.Formatter(
    "%(asctime)s :: %(levelname)s :: [%(filename)s:%(lineno)s:%(funcName)s()] :: %(message)s"
)
file_handler = RotatingFileHandler(
    DIR_LOGS
    + LOGGER_NAME
    + "_"
    + dt.datetime.now().strftime("%Y-%m-%d_%H-%M")
    + ".log",
    "a",
    100_000_000,
    1,
    encoding="utf-8"
)
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(formatter)
_logger.addHandler(file_handler)
