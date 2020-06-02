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
        self.connect_db = ConnectionDB().cursor

    def autefication_users(self, name_secret: tuple) -> bool:
        """ For authentification of the users  """
        self.connect_db.execute("SELECT username, password FROM users")
        username = name_secret[0]
        usersecret = name_secret[1]
        respons_serv = self.connect_db.fetchall()
        print('Я в autefication_users', respons_serv)

        for step in respons_serv:
            if username == step[0]:
                if usersecret == step[1]:
                    return True 
                else:      
                    return False



    def get_all_users(self) -> dict:
        """ This function can get all the users from DB """
        # !!!!!!!!!!!!!!!!!!!!!!!! TOdo кол-во досок!!!!!!!!
        respons = {
                    "count": '',
                    "users": []
                    }

        self.connect_db.execute("SELECT username, password FROM users")
        respons_serv = self.connect_db.fetchall()

        for step in respons_serv:
            respons["users"].append({"username": step[0]})
        return respons




    def board_create(self, data: dict):
        """ For create a new board """

        self.connect_db.execute("CREATE TABLE ")
