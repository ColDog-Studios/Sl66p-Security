import os
import yaml

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                self.config = yaml.safe_load(file)
        else:
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save_config(self):
        with open(self.config_path, 'w') as file:
            yaml.dump(self.config, file)