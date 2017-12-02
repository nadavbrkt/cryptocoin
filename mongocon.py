import pymongo
from conf import Conf

class MongoCon:
    _mongoclient = pymongo.MongoClient()

    def __init__(self, username, password, ip, port = 27017):
        conf = Conf()
        self.username = self.username
        self.password = password
        self.ip = ip
        self.port = port

        