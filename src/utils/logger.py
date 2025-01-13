import logging
import os
import yaml

class Logger:
    def __init__(self, name, config_path='config/logging_config.yaml'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._configure_logger(config_path)

    def _configure_logger(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                logging.config.dictConfig(config)
        else:
            self.logger.warning(f"Logging configuration file not found: {config_path}")

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

def setup_logging(name, config_path='config/logging_config.yaml'):
    return Logger(name, config_path)