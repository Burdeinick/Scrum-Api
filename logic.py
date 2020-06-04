import psycopg2
from contextlib import closing
import time

dbname = "t_managing_db"
user = "alex"
password = "0525"


class ConnectionDB:
    """ """
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()


class RequestsDB:
    """ """
    def __init__(self):
        self.connect_db = ConnectionDB().cursor
        self.conn = ConnectionDB().conn

    def request_get_all_users(self) -> list:
        """ """
        self.connect_db.execute("SELECT username, password FROM users")
        return self.connect_db.fetchall()

    def request_create_new_board(self, collecte_data: tuple):



        self.connect_db.execute(f"INSERT INTO boards(title, \
                                                    columns, \
                                                    created_at, \
                                                    created_by, \
                                                    last_updated_at, \
                                                    last_updated_by)  \
                                  values('{collecte_data[0]}', \
                                         '{collecte_data[1]}', \
                                         '{collecte_data[2]}', \
                                         '{collecte_data[3]}', \
                                         '{collecte_data[4]}', \
                                         '{collecte_data[5]}')")

        self.conn.commit()
        print(self.connect_db.statusmessage)

        # self.connect_db.execute("SELECT * FROM boards")


class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.req_DB = RequestsDB()

    def autefication_users(self, name_secret: tuple) -> bool:
        """ For authentification of the users  """
        username = name_secret[0]
        usersecret = name_secret[1]
        
        respons_of_DB = self.req_DB.request_get_all_users()
        print('Я в autefication_users', respons_of_DB)
        for step in respons_of_DB:
            if username == step[0]:
                if usersecret == step[1]:
                    return True 
                else:      
                    return False

    def get_all_users(self) -> dict:
        """ This function can get all the users from DB """
        # !!!!!!!!!!!!!!!!!!!!!!!! TOdo кол-во досок!!!!!!!!
        respons_to_serv = {
                            "count": '',
                            "users": []
                            }

        respons_of_DB = self.req_DB.request_get_all_users()

        for step in respons_of_DB:
            respons_to_serv["users"].append({"username": step[0]})
        return respons_to_serv




    def create_new_board(self, data: dict, username: str):
        """ For create a new board """

        title = data["title"]
        colums = ' '.join(data["columns"])
        created_at = time.time()
        created_by = username
        last_updated_at =  time.time()
        last_updated_by = username

        collecte_data = (
                         title,
                         colums,
                         created_at,
                         created_by,
                         last_updated_at,
                         last_updated_by
                        )

        self.req_DB.request_create_new_board(collecte_data)
        
