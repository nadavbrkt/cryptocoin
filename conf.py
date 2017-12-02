# TODO: Create conf file template
import yaml
from utils import Singleton
import os

conf_file_path = (".\conf\conf.yml",)

class Conf:
    __metaclass__ = Singleton
    _configuration = {}

    def __init__(self,):
        for path in conf_file_path:
            if os.path.isfile(path):
                file_ = open(path, "r")
                break;

        self._configuration = yaml.load(file_)

    def get_db_user(self):
        return self._configuration["db"]["user"]

    def get_db_password(self):
        return self._configuration["db"]["password"]

    def get_db_hostname(self):
        return self._configuration["db"]["host"]

    def get_db_port(self):
        return self._configuration["db"]["port"]

    def get_db_name(self):
        return self._configuration["db"]["name"]

    def get_connection_string(self):
        return "" + self._configuration["db"]["host"] \
               + ":" + self._configuration["db"]["port"] \
               + "/" + self._configuration["db"]["name"]





