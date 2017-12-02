import pymongo
from conf import Conf
from utils import Singleton
import urllib

class MongoCon:
    __metaclass__ = Singleton
    _connection = ""

    def __init__(self):
        conf = Conf()
        username = urllib.quote("" + conf.get_db_user())
        password = urllib.quote("" + conf.get_db_password())

        connection = pymongo.MongoClient("mongodb://" \
                                         + username + ":" + password \
                                         + "@" + conf.get_connection_string())

        self._connection = connection
        self.db = self._connection[conf.get_db_name()]

    def __del__(self):
        self._connection.close()

    def get_stuff(self):
        print self.db.log.find_one()