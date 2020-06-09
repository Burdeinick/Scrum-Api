import psycopg2
from contextlib import closing
import time
from datetime import datetime

dbname = "t_managing_db"
user = "alex"
password = "0525"


class Statuses:
    """The statuses of answers is here."""
    def __init__(self):
        self.aut_error = {"status":"Authentification Error."}
        self.user_no_avaib = {"status": "No users available"} 
        self.such_board_exists = {"status": "This a board already exist."}
        self.board_create = {"status": "The board was created."}
        self.board_not_create = {"status": "The new board was don't created."}
        self.board_delete = {"status": "The board was delete."}
        self.board_not_delete = {"status": "The board was don't delete."}
        self.board_not_exist = {"status": "This a board does not exist."}
        self.boards_not_exist = {"Status": "A boards don't exist."}
        self.such_card_exist = {"status": "This a card already exist на данной доске."}
        self.card_create = {"status": "The card was created."}
        self.card_not_create = {"status": "The new card was don't created."}
        self.card_not_create_board = {"status": "The new card was don't created, such board no exist."}
        self.card_not_update_disc = {"status": "The card has not been updated."}
        self.card_update = {"status": "The card has updated."}
        self.card_not_update = {"status": "The card has not been updated."}
        self.card_not_exist = {"status": "The card does not exist."}
        self.card_delete = {"status": "The card has delete."}
        self.card_not_delete = {"status": "The card has not been deleted."}
        self.colum_not_info = {"status": "The information about these columns are absent."}


class ConnectionDB:
    """Class for connect to DB."""
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()


class RequestsDB:
    """Class for requests DB."""
    def __init__(self):
        self.connect_db = ConnectionDB()
        self.stat = Statuses()

    def request_get_all_users(self) -> list:
        """ """
        self.connect_db.cursor.execute("SELECT username, password FROM users")
        return self.connect_db.cursor.fetchall()








    def request_one_user(self, username: str, usersecret: str ) -> list:
        """ """
        request = f"SELECT username  \
                    FROM users \
                    WHERE (username='{username}') AND (password='{usersecret}')"

        self.connect_db.cursor.execute(request)
        return self.connect_db.cursor.fetchall()









    def request_create_board(self, collecte_data: tuple) -> bool:
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
        """ """
        request = f"SELECT title    \
                    FROM boards"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()

    

















    def request_one_board(self, title: str) -> list:
        """For checking this board."""
        request = f"SELECT title    \
                    FROM boards \
                    WHERE title='{title}'"

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
                            last_updated_by \
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

    def request_str_title_board(self, title, board):
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
                            last_updated_by \
                    FROM cards \
                    WHERE(title LIKE '{title}') AND (board LIKE '{board}');"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()        

    def request_card_update(self, collecte_data: list):
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

        print(collecte_data)

        request = f"UPDATE cards \
                    SET status = '{status}', \
                        description = '{description}', \
                        assignee = '{assignee}', \
                        estimation = '{estimation}', \
                        created_at = '{created_at}', \
                        created_by = '{created_by}', \
                        last_updated_at = '{last_updated_at}', \
                        last_updated_by = '{last_updated_by}' \
                        WHERE(title='{title}') AND (board='{board}');"

        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        respons = self.connect_db.cursor.statusmessage
        if respons == "UPDATE 1":
            return True
        return False
 
    def request_card_delete(self, title, board):
        """ """
        request = f"DELETE FROM cards \
                    WHERE (title='{title}') AND (board='{board}')"

        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        respons = self.connect_db.cursor.statusmessage
        print(respons)
        if respons == "DELETE 1":
            return True
        return False

    def request_get_info_column(self, board, status, assignee):
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
                    last_updated_by \
                    FROM cards \
                    WHERE (board='{board}') AND (status='{status}') AND (assignee='{assignee}');"

        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall() 


class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.req_DB = RequestsDB()
        self.stat = Statuses()

































# Переделать для поиска конкретного пользователя пользователя в БД

    def autefication_users(self, name_secret: tuple) -> bool:
        """ For authentification of the users """
        username = name_secret[0]
        usersecret = name_secret[1]
        respons_db = self.req_DB.request_one_user(username, usersecret)
        if respons_db:
            return True
        return False

















































    def get_all_users(self) -> dict:
        """This function can get all the users from DB."""
        respons_to_serv = {"users": []}
        respons_db = self.req_DB.request_get_all_users()
        if not respons_db:
            return self.stat.user_no_avaib

        for step in respons_db:
            username = step[0]
            respons_to_serv["users"].append({"username": username})
        return respons_to_serv


    def create_board(self, data: dict, head: dict) -> dict:
        """For create a new board."""
        username = str(head['UserName'])
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

        resp_db = self.req_DB.request_one_board(title)
        if resp_db:
            return self.stat.such_board_exists

        if self.req_DB.request_create_board(collecte_data):
            return self.stat.board_create
        return self.stat.board_not_create

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
                    return self.stat.board_delete

                if not self.req_DB.request_delete_board(title): 
                    print('Доска не удалена')
                    return self.stat.board_not_delete
        print('Доска не удалена', {"status": "This a board does not exist"})
        return self.stat.board_not_exist

    def get_all_boars(self):
        """ This function can get all the boards from DB"""
        respons_of_DB_exist_board = self.req_DB.request_check_board_avail()
        print("Я в get_all_boars", respons_of_DB_exist_board)
        if respons_of_DB_exist_board == []:
            print('Список пуст, досок нет')
            return self.stat.boards_not_exist
            
        if len(respons_of_DB_exist_board) >= 1:
            print('Список полон')
            print(self.req_DB.request_get_all_boards())
            response_to_serv = {"count": None, "boards": [] }
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










    def create_cards(self, data: dict, username: str):
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
           
        respons_one_bord = self.req_DB.request_one_board(board)  # Проверка на наличие доски в БД к которой хотим привязать карточку
        if not respons_one_bord:
            print("Карточка не создана, доска с указанным названием в БД не существует")
            return self.stat.card_not_create_board

        respons_of_DB_card = self.req_DB.request_get_title_board_for_card()  # Проверка на наличие уже существующей такой карточки на указанной доске в БД

        for titl_boar in respons_of_DB_card:
            title_DB, board_DB = titl_boar[0], titl_boar[1],

            if (title == title_DB) and (board == board_DB):
                print(f"1 Карточка с названием '{title}'' на доске '{board}' уже существет.")
                return self.stat.such_card_exist

        if self.req_DB.request_create_card(collecte_data):
            print('2', {"status": "The card was created"})
            return self.stat.card_create

        print('3', {"status": "The new card was don't created"})
        return self.stat.card_not_create









    def update_card(self, data: dict, username: str) -> dict:
        """For update a card."""
        title = data["title"]
        board = data["board"]
        status = data.get("status")
        description = data.get("description")
        assignee = data.get("assignee")
        estimation = data.get("estimation")
        # делаю запрос с конкретным where title LIKE и тд.
        resp_DB_title_board = self.req_DB.request_str_title_board(title, board)[0]
        if not resp_DB_title_board:
            print("Несопоставление карточки и доски")
            return self.stat.card_not_update_disc

        collecte_data = [title, board]
        if status != None:
            collecte_data.append(status)
        else:
            collecte_data.append(resp_DB_title_board[2])

        if description != None:
            collecte_data.append(description)
        else:
            collecte_data.append(resp_DB_title_board[3])

        if assignee != None:
            collecte_data.append(assignee)
        else:
            collecte_data.append(resp_DB_title_board[4])   

        if estimation != None:
            collecte_data.append(estimation)
        else:
            collecte_data.append(resp_DB_title_board[5])   

        collecte_data.append(resp_DB_title_board[6])
        collecte_data.append(resp_DB_title_board[7])
        collecte_data.append(int(time.time()))
        collecte_data.append(username)

        respons_to_serv = self.req_DB.request_card_update(collecte_data)
        if respons_to_serv:
            print('Карточка обновлена!')
            return self.stat.card_update
        print('Карточка не обновлена!')  
        return self.stat.card_not_update
        
    def card_delete(self, data):
        """For delete a card."""
        title = data["title"]
        board = data["board"]
        resp_of_DB = self.req_DB.request_str_title_board(title, board)
        if not resp_of_DB:
            print('Tакой карточки не сущесвует')
            return self.stat.card_not_exist
        
        card_delete = self.req_DB.request_card_delete(title, board)
        if card_delete:
            print('Карточка удалена')
            return self.stat.card_delete

        print('Карточка не удалена !!!')   
        return self.stat.card_not_delete


    def column_info(self, data):
        """ """
        board = data["board"]
        column = data["column"]
        assignee = data["assignee"]

        resp_DB = self.req_DB.request_get_info_column(board, column, assignee)

        if not resp_DB:
            return self.stat.colum_not_info

        response_dict = {"board": board,
                         "column": column,
                         "assignee": assignee,
                         "count": len(resp_DB),
                         "estimation": None,
                         "cards": []
                        }

        for card in resp_DB:
            title = card[0]
            board = card[1]
            status = card[2]
            description = card[3]
            assignee = card[4]
            estimation = card[5]
            created_at = str(datetime.fromtimestamp(int(card[6])))
            created_by = card[7]
            last_updated_at = str(datetime.fromtimestamp(int(card[8])))
            last_updated_by =card[9]

            card_dict = {
                        "title": title,
                        "board": board,
                        "status": status,
                        "description": description,
                        "assignee": assignee, 
                        "estimation": estimation, 
                        "created_at": created_at,
                        "created_by": created_by,
                        "last_updated_at": last_updated_at,
                        "last_updated_by": last_updated_by
                        }
            response_dict["cards"].append(card_dict)
        return response_dict