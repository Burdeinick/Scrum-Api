import psycopg2
from contextlib import closing

dbname = 't_managing_db'
user = 'alex' 
password = '0525' 
host = 'localhost'


class ServerProcessing:
    """ """
    def __init__(self ):
        pass


class ConnectionDB:
    """ """
    def __init__(self):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        """ """
        conn = psycopg2.connect(self.dbname, self.user,
                                self.password, self.host)


class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.connect_db = ConnectionDB()

    def autefication_users(self, name_secret: tuple) -> bool:
        """ """
        return
    
    def get_all_users(self):
        """ This function can get all the users from DB """
        # conn = psycopg2.connect()


#