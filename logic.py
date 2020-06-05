import psycopg2
from contextlib import closing
import time

dbname = "t_managing_db"
user = "alex"
password = "0525"


class Statuses:
    """ """
    def __init__(self):
        self.such_board_exists = {"status": "This a board already exist"}
        self.new_board_create = {"status": "The board was created"}
        self.new_board_dont_create = {"status": "The new board was don't created"}
        self.authentif_error = {"Authentification": "Error"}

class ConnectionDB:
    """ """
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password)
        self.cursor = self.conn.cursor()


class RequestsDB:
    """ """
    def __init__(self):
        self.connect_db = ConnectionDB()
        self.statuses = Statuses()

    def request_get_all_users(self) -> list:
        """ """
        self.connect_db.cursor.execute("SELECT username, password   \
                                        FROM users")
        return self.connect_db.cursor.fetchall()

    def request_create_new_board(self, collecte_data: tuple):
        """ The function for requests to DB for adding new board in "boards" table. """
        title = collecte_data[0]
        columns = collecte_data[1]
        created_at = collecte_data[2]
        created_by = collecte_data[3]
        last_updated_at = collecte_data[4]
        last_updated_by = collecte_data[5]

        request = f"INSERT INTO boards(                     \
                                        title,              \
                                        columns,            \
                                        created_at,         \
                                        created_by,         \
                                        last_updated_at,    \
                                        last_updated_by     \
                                        )                   \
                    values(                       \
                            '{title}',            \
                            '{columns}',          \
                            '{created_at}',       \
                            '{created_by}',       \
                            '{last_updated_at}',  \
                            '{last_updated_by}'   \
                            )"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return self.statuses.new_board_create
        return self.statuses.new_board_dont_create

    def request_check_board_avail(self):
        request = f"SELECT title    \
                    FROM boards"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        return self.connect_db.cursor.fetchall()


class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.req_DB = RequestsDB()
        self.statuses = Statuses()

    def autefication_users(self, name_secret: tuple) -> bool:
        """ For authentification of the users  """
        username = name_secret[0]
        usersecret = name_secret[1]
        
        respons_of_DB = self.req_DB.request_get_all_users()
        # print('Я в autefication_users', respons_of_DB)
        for step in respons_of_DB:
            if username == step[0]:
                if usersecret == step[1]:
                    return True 
                else:      
                    return False

    def get_all_users(self) -> dict:
        """ This function can get all the users from DB """
        # !!!!!!!!!!!!!!!!!!!!!!!! TOdo кол-во досок!!!!!!!!
        respons_to_serv = {"users": []}

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


        respons_of_DB_same_title = self.req_DB.request_check_board_avail()  # Проверка на наличие такой доски в БД
        print()

        for title_in_DB in respons_of_DB_same_title:
            if title_in_DB[0] ==  title:
                print('1', 'Доска не создалась!', {"status": "This a board already exist"})
                return self.statuses.such_board_exists

            if self.req_DB.request_create_new_board(collecte_data):
                print('2', {"status": "The board was created"})
                return self.statuses.such_board_exists

        print('3', {"status": "The new board was don't created"})
        return self.statuses.new_board_dont_create
        