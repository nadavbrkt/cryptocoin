from coin import Coin
from conf import Conf
from mongocon import MongoCon

if __name__ == "__main__":
    c = Conf()
    print c.get_db_hostname()

    mon = MongoCon()

    mon.get_stuff()
