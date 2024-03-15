from configparser import ConfigParser, NoSectionError
import os

def validate_config(config: ConfigParser):
    if 'file_paths' not in config.sections():
        raise NoSectionError(f'file_paths section not found in configuration file')
    if 'apriori_params' not in config.sections():
        raise NoSectionError(f'apriori_params section not found in configuration file')

def load_config() -> ConfigParser:
    config = ConfigParser()
    config_filepath = os.environ['CONFIG_FILEPATH']

    if not config_filepath or not os.path.isfile(config_filepath):
        raise FileNotFoundError(f"The configuration file was not found")

    config.read(config_filepath)
    validate_config(config)
    return config

config = load_config()