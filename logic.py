import psycopg2
from contextlib import closing

dbname = "t_managing_db"
user = "alex"
password = "0525"


class ServerProcessing:
    """ """
    def __init__(self ):
        pass


class ConnectionDB:
    """ """
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()



class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.connect_db = ConnectionDB()

    def autefication_users(self, name_secret: tuple) -> bool:
        """ """

        return True
    
    def get_all_users(self):
        """ This function can get all the users from DB """
        # conn = psycopg2.connect()


#