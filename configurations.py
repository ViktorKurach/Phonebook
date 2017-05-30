from configparser import RawConfigParser


class Config:
    """
    class for parsing cfg file with configs
    """
    config = None

    def __init__(self):
        """
        init ConfigParser and read file with configs
        """
        self.config = RawConfigParser()
        self.config.read('serialize_conf.cfg')

    def get_setting(self, config_section, config_key):
        """
        return config from file by config section and config key
        """
        return self.config.get(config_section, config_key)
