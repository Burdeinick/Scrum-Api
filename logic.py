import psycopg2
from contextlib import closing
import time
from datetime import datetime

dbname = "t_managing_db"
user = "alex"
password = "0525"


class Statuses:
    """ """
    def __init__(self):
        self.authentif_error = {"Authentification": "Error"}

        self.such_board_exists = {"status": "This a board already exist"}
        self.new_board_create = {"status": "The board was created"}
        self.new_board_dont_create = {"status": "The new board was don't created"}
        self.board_delete = {"status": "The board was delete"}
        self.board_dont_delete = {"status": "The board was don't delete"}
        self.board_doesnot_exist = {"status": "This a board does not exist"}
        self.boards_donot_exist = {"Status": "A boards don't exist"}

        self.such_card_exist = {"status": "This a card already exist на данной доске"}
        self.card_create = {"status": "The card was created"}
        self.card_dont_create = {"status": "The new card was don't created"}
        self.card_dont_create_board_notexist = {"status": "The new card was don't created, such board no exist"}


class ConnectionDB:
    """ """
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
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

    def request_create_new_board(self, collecte_data: tuple) -> bool:
        """ The function for requests to DB for adding new board in "boards" table. """
        title = collecte_data[0]
        columns = collecte_data[1]
        created_at = collecte_data[2]
        created_by = collecte_data[3]
        last_updated_at = collecte_data[4]
        last_updated_by = collecte_data[5]

        request = f"INSERT INTO boards( \
                                        title,\
                                        columns,\
                                        created_at,\
                                        created_by,\
                                        last_updated_at,\
                                        last_updated_by\
                                        )\
                    values(                       \
                            '{title}',            \
                            '{columns}',          \
                            '{created_at}',       \
                            '{created_by}',       \
                            '{last_updated_at}',  \
                            '{last_updated_by}'   \
                            );"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return True
        return False

    def request_check_board_avail(self):
        request = f"SELECT title    \
                    FROM boards"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()

    def request_delete_board(self, title: str):
        """ """
        request = f"DELETE FROM boards    \
                    WHERE title='{title}';"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        if self.connect_db.cursor.statusmessage == "DELETE 1":
            return True
        return False






    def request_get_all_boards(self) -> list:
        """ """
        request = f"SELECT title,               \
                            columns,            \
                            created_at,         \
                            created_by,         \
                            last_updated_at,    \
                            last_updated_by     \
                    FROM boards"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()













    def request_get_title_board_for_card(self):
        """ """
        request = f"SELECT title, \
                            board, \
                            status, \
                            description, \
                            assignee, \
                            estimation, \
                            created_at, \
                            created_by, \
                            last_updated_at, \
                            last_updated_by, \
                    FROM cards"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()









    def request_create_card(self, collecte_data: tuple) -> bool:
        """ """
        title = collecte_data[0]
        board = collecte_data[1]
        status = collecte_data[2]
        description = collecte_data[3]
        assignee = collecte_data[4]
        estimation = collecte_data[5]
        created_at = collecte_data[6]
        created_by = collecte_data[7]
        last_updated_at = collecte_data[8]
        last_updated_by = collecte_data[9]

        request = f"INSERT INTO cards(          \
                                        title,\
                                        board,\
                                        status,\
                                        description,\
                                        assignee,\
                                        estimation,\
                                        created_at,\
                                        created_by,\
                                        last_updated_at,\
                                        last_updated_by\
                                        )\
                    values(  \
                            '{title}',\
                            '{board}',\
                            '{status}',\
                            '{description}',\
                            '{assignee}',\
                            '{estimation}',\
                            '{created_at}', \
                            '{created_by}',\
                            '{last_updated_at}',\
                            '{last_updated_by}'\
                            );"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return True
        return False







































class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.req_DB = RequestsDB()
        self.statuses = Statuses()

    def autefication_users(self, name_secret: tuple) -> bool:
        """ For authentification of the users """
        username = name_secret[0]
        usersecret = name_secret[1]
        
        respons_of_DB = self.req_DB.request_get_all_users()
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
            print(respons_to_serv)
        return respons_to_serv

    def create_new_board(self, data: dict, username: str):
        """For create a new board."""
        title = str(data["title"])
        colums = str(' '.join(data["columns"]))
        created_at = str(int(time.time()))
        created_by = str(username)
        last_updated_at =  str(int(time.time()))
        last_updated_by = str(username)

        collecte_data = (
                         title,
                         colums,
                         created_at,
                         created_by,
                         last_updated_at,
                         last_updated_by
                        )

        respons_of_DB = self.req_DB.request_check_board_avail()  # Проверка на наличие такой доски в БД

        for title_in_DB in respons_of_DB:
            if title_in_DB[0] ==  title:
                print('1', 'Доска не создалась!', {"status": "This a board already exist"})
                return self.statuses.such_board_exists

        if self.req_DB.request_create_new_board(collecte_data):
            print('2', {"status": "The board was created"})
            return self.statuses.new_board_create

        print('3', {"status": "The new board was don't created"})
        return self.statuses.new_board_dont_create
        
    def delete_board(self, data: dict):
        """For delete the board."""
        title = str(data["title"])

        respons_of_DB_board_avai = self.req_DB.request_check_board_avail()
        print(respons_of_DB_board_avai)
        for title_in_DB in respons_of_DB_board_avai:
            if title_in_DB[0] ==  title:
                print('Доска найдена, отправлю запрос на удаление такой доски!')

                if self.req_DB.request_delete_board(title):
                    print('Доска удалена')
                    return self.statuses.board_delete

                if not self.req_DB.request_delete_board(title): 
                    print('Доска не удалена')
                    return self.statuses.board_dont_delete
        print('Доска не удалена', {"status": "This a board does not exist"})
        return self.statuses.board_doesnot_exist

    def get_all_boars(self):
        """ This function can get all the boards from DB"""
        respons_of_DB_exist_board = self.req_DB.request_check_board_avail()
        print("Я в get_all_boars", respons_of_DB_exist_board)
        if respons_of_DB_exist_board == []:
            print('Список пуст, досок нет')
            return self.statuses.boards_donot_exist
            
        if len(respons_of_DB_exist_board) >= 1:
            print('Список полон')
            print(self.req_DB.request_get_all_boards())
            response_to_serv = {
                                "count": None, 
                                "boards": []    
                                }
            for step_tuple in self.req_DB.request_get_all_boards():
                count = str(len(respons_of_DB_exist_board))
                board = str(step_tuple[0])
                created_at = str(datetime.fromtimestamp(int(step_tuple[2])))  # Переделать чтобы при создании таблицы boards эта колонка была int
                created_by = str(step_tuple[3])
                last_updated_at = str(datetime.fromtimestamp(int(step_tuple[4])))
                last_updated_by = str(step_tuple[5])

                d_board = {}
                d_board["board"] = board
                d_board["created_at"] = created_at
                d_board["created_by"] = created_by
                d_board["last_updated_at"] = last_updated_at
                d_board["last_updated_by"] = last_updated_by

                response_to_serv["count"] = count
                response_to_serv["boards"].append(d_board)

            print(f"Отправил {response_to_serv}")
            return response_to_serv



    def create_new_cards(self, data: dict, username: str):
        """For create a new card."""
        response_to_serv = None
        title = data["title"]
        board = data["board"]
        status = data["status"]
        description = data["description"]
        assignee = data["assignee"]
        estimation = data["estimation"]
        created_at = int(time.time())
        created_by = str(username)
        last_updated_at = int(time.time())
        last_updated_by = str(username)

        collecte_data = (
                         title,
                         board,
                         status,
                         description,
                         assignee,
                         estimation,
                         created_at,
                         created_by,
                         last_updated_at,
                         last_updated_by,
                        )
           
        respons_of_DB_boards = self.req_DB.request_get_all_boards()   # Проверка на наличие доски в БД к которой хотим привязать карточку

        for tup_board in respons_of_DB_boards:
            board_DB = tup_board[0]
            if board != board_DB:
                print("Карточка не создана, доска с указанным названием в БД не существует")
                return self.statuses.card_dont_create_board_notexist

        respons_of_DB_card = self.req_DB.request_get_title_board_for_card()  # Проверка на наличие уже существующей такой карточки на указанной доске в БД

        for titl_boar in respons_of_DB_card:
            title_DB, board_DB = titl_boar[0], titl_boar[1],

            if (title == title_DB) and (board == board_DB):
                print(f"1 Карточка с названием '{title}'' на доске '{board}' уже существет.")
                return self.statuses.such_card_exist

        if self.req_DB.request_create_card(collecte_data):
            print('2', {"status": "The card was created"})
            return self.statuses.card_create

        print('3', {"status": "The new card was don't created"})
        return self.statuses.card_dont_create




    def update_card(self, data: dict, username: str) -> dict:
        """For update a card."""
        title = data["title"]
        board = data["board"]

        status = data.get("status")
        description = data.get("description")
        assignee = data.get("assignee")
        estimation = data.get("estimation")
  
        # collecte_data = (
        #                  title,
        #                  board,
        #                  status,
        #                  description,
        #                  assignee,
        #                  estimation
        #                 )

        # response_DB_card_str = self.req_DB.request_get_title_board_for_card() ??? надо ли
        
        # сделать запрос с конкретным where title LIKE и тд.

        lst_update = (title, board)

        if status != None:
            lst_update.append(status)
        else:
            lst_update.append(#)

        if description != None:
            lst_update.append(description)
        else:
            lst_update.append(#)

        if assignee != None:
            lst_update.append(assignee)
        else:
            lst_update.append(#)   

        if estimation != None:
            lst_update.append(estimation)
        else:
            lst_update.append(#)   

        lst_update.append(#)
        lst_update.append(#)
        lst_update.append(int(time.time))
        lst_update.append(username)

        