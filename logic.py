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
        self.board_delete = {"status": "The board removed."}
        self.board_not_delete = {"status": "The board was don't delete."}
        self.board_not_exist = {"status": "This a board does not exist."}
        self.boards_not_exist = {"Status": "A boards don't exist."}
        self.such_card_exist = {"status": "This a card already exist at this board."}
        self.card_create = {"status": "The card created."}
        self.card_not_create = {"status": "The new card was don't created."}
        self.card_not_create_board = {"status": "The new card was don't created, such board no exist."}
        self.card_not_match = {"status": "The 'Board' and the 'title' have not match."}
        self.card_update = {"status": "The card has updated."}
        self.card_not_update = {"status": "The card has not been updated."}
        self.card_not_exist = {"status": "The card does not exist."}
        self.card_delete = {"status": "The card removed."}
        self.card_not_delete = {"status": "The card has not been deleted."}
        self.colum_not_info = {"status": "The information about these columns are absent."}

        def __str__(self):
            return __class__.__name__


class ConnectionDB:
    """Class for connect to DB."""
    def __init__(self):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        self.cursor = self.conn.cursor()

    def __str__(self):
        return __class__.__name__


class RequestsDB:
    """Class for requests DB."""
    def __init__(self):
        self.connect_db = ConnectionDB()
        self.stat = Statuses()

    def __str__(self):
        return __class__.__name__

    def request_get_all_users(self) -> list:
        """This function returning of list all the users."""
        self.connect_db.cursor.execute("SELECT username FROM users")
        return self.connect_db.cursor.fetchall()

    def request_authen_user(self, username: str, usersecret: str ) -> list:
        """This function checking authentification user."""
        request = f"SELECT username \
                    FROM users      \
                    WHERE (username='{username}') AND (password='{usersecret}')"
        self.connect_db.cursor.execute(request)
        return self.connect_db.cursor.fetchall()

    def request_create_board(self, collecte_data: tuple) -> bool:
        """The function for requests to DB for adding new board in "boards" table."""
        title = collecte_data[0]
        columns = collecte_data[1]
        created_at = collecte_data[2]
        created_by = collecte_data[3]
        last_updated_at = collecte_data[4]
        last_updated_by = collecte_data[5]

        request = f"INSERT INTO boards(                  \
                                        title,           \
                                        columns,         \
                                        created_at,      \
                                        created_by,      \
                                        last_updated_at, \
                                        last_updated_by  \
                                        )                \
                    values(                         \
                            '{title}',              \
                            '{columns}',            \
                            '{created_at}',         \
                            '{created_by}',         \
                            '{last_updated_at}',    \
                            '{last_updated_by}'     \
                            );"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()
        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return True
        return False

    def request_one_board(self, title: str) -> list:
        """For checking this board."""
        request = f"SELECT title    \
                    FROM boards     \
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
        """This function returns list of the boards."""
        request = f"SELECT title,               \
                            columns,            \
                            created_at,         \
                            created_by,         \
                            last_updated_at,    \
                            last_updated_by     \
                    FROM boards"
        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()

    def request_title_board(self, title: str, board: str) -> list:
        """The function checking 'title' and 'board' in one string."""
        request = f"SELECT title,               \
                            board,              \
                            status,             \
                            description,        \
                            assignee,           \
                            estimation,         \
                            created_at,         \
                            created_by,         \
                            last_updated_at,    \
                            last_updated_by     \
                    FROM cards                  \
                    WHERE (title='{title}') AND (board='{board}')"
        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall()

    def request_create_card(self, collecte_data: tuple) -> bool:
        """The function for creating a card."""
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

        request = f"INSERT INTO cards(                      \
                                        title,              \
                                        board,              \
                                        status,             \
                                        description,        \
                                        assignee,           \
                                        estimation,         \
                                        created_at,         \
                                        created_by,         \
                                        last_updated_at,    \
                                        last_updated_by     \
                                        )           \
                    values(                         \
                            '{title}',              \
                            '{board}',              \
                            '{status}',             \
                            '{description}',        \
                            '{assignee}',           \
                            '{estimation}',         \
                            '{created_at}',         \
                            '{created_by}',         \
                            '{last_updated_at}',    \
                            '{last_updated_by}'     \
                            )"

        self.connect_db.cursor.execute(request)                                       
        self.connect_db.conn.commit()

        if self.connect_db.cursor.statusmessage == "INSERT 0 1":
            return True
        return False

    def request_card_update(self, collecte_data: list) -> bool:
        """The function for updating a card."""
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
        request = f"UPDATE cards                                \
                    SET status = '{status}',                    \
                        description = '{description}',          \
                        assignee = '{assignee}',                \
                        estimation = '{estimation}',            \
                        created_at = '{created_at}',            \
                        created_by = '{created_by}',            \
                        last_updated_at = '{last_updated_at}',  \
                        last_updated_by = '{last_updated_by}'   \
                        WHERE(title='{title}') AND (board='{board}')"

        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        respons = self.connect_db.cursor.statusmessage
        if respons == "UPDATE 1":
            return True
        return False
 
    def request_card_delete(self, title: str, board: str) -> bool:
        """For request about delete a card."""
        request = f"DELETE FROM cards \
                    WHERE (title='{title}') AND (board='{board}')"
        self.connect_db.cursor.execute(request)
        self.connect_db.conn.commit()
        respons = self.connect_db.cursor.statusmessage
        if respons == "DELETE 1":
            return True
        return False

    def request_info_column(self, board: str, status: str, assignee: str) -> list:
        """For request about the column."""
        request = f"SELECT title,       \
                    board,              \
                    status,             \
                    description,        \
                    assignee,           \
                    estimation,         \
                    created_at,         \
                    created_by,         \
                    last_updated_at,    \
                    last_updated_by     \
                    FROM cards          \
                    WHERE (board='{board}') AND (status='{status}') AND (assignee='{assignee}');"
        self.connect_db.cursor.execute(request)                                       
        return self.connect_db.cursor.fetchall() 


class UsingDB:
    """ """
    def __init__(self, data=None):
        self.data = data
        self.req_DB = RequestsDB()
        self.stat = Statuses()

    def autefication_users(self, name_secret: tuple) -> bool:
        """For authentification of the users."""
        username = name_secret[0]
        usersecret = name_secret[1]
        respons_db = self.req_DB.request_authen_user(username, usersecret)
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

    def delete_board(self, data: dict) -> dict:
        """For delete the board."""
        title = str(data["title"])
        respons_db = self.req_DB.request_one_board(title)
        if not respons_db:
            return self.stat.board_not_exist
        respons_db_del = self.req_DB.request_delete_board(title)   
        if respons_db_del:
            return self.stat.board_delete
        if respons_db_del: 
            return self.stat.board_not_delete

    def get_all_boars(self) -> dict:
        """This function can get all the boards from DB."""
        respons_db = self.req_DB.request_get_all_boards()
        if not respons_db:
            return self.stat.boards_not_exist
        response_to_serv = {"count": None, "boards": [] }
        for values in respons_db:
            count = str(len(respons_db))
            board = str(values[0])
            created_at = str(datetime.fromtimestamp(int(values[2])))
            created_by = str(values[3])
            last_updated_at = str(datetime.fromtimestamp(int(values[4])))
            last_updated_by = str(values[5])
            d_board = {}
            d_board["board"] = board
            d_board["created_at"] = created_at
            d_board["created_by"] = created_by
            d_board["last_updated_at"] = last_updated_at
            d_board["last_updated_by"] = last_updated_by
            response_to_serv["count"] = count
            response_to_serv["boards"].append(d_board)
        return response_to_serv

    def create_cards(self, data: dict, head: dict) -> dict:
        """For create a new card."""
        username = str(head['UserName'])
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
        # проверка существования такой доски 
        respons_db_board = self.req_DB.request_one_board(board)
        if not respons_db_board:
            return self.stat.card_not_create_board
        # проверка если есть уже такая карта с такой доской
        respons_db_card = self.req_DB.request_title_board(title, board)
        if respons_db_card:
            return self.stat.such_card_exist
        # создается доска
        response_db_create_card = self.req_DB.request_create_card(collecte_data)
        if response_db_create_card:
             return self.stat.card_create
        return self.stat.card_not_create

    def update_card(self, data: dict, head: dict) -> dict:
        """For update a card."""
        username = str(head['UserName'])
        title = data["title"]
        board = data["board"]
        status = data.get("status")
        description = data.get("description")
        assignee = data.get("assignee")
        estimation = data.get("estimation")

        response_db = self.req_DB.request_title_board(title, board)
        if not response_db:
            return self.stat.card_not_match

        collecte_data = [title, board]
        card = response_db[0]
        if status != None:
            collecte_data.append(status)
        else:
            collecte_data.append(card[2])
        if description != None:
            collecte_data.append(description)
        else:
            collecte_data.append(card[3])
        if assignee != None:
            collecte_data.append(assignee)
        else:
            collecte_data.append(card[4])   
        if estimation != None:
            collecte_data.append(estimation)
        else:
            collecte_data.append(card[5])   

        collecte_data.append(card[6])
        collecte_data.append(card[7])
        collecte_data.append(int(time.time()))
        collecte_data.append(username)

        respons_to_serv = self.req_DB.request_card_update(collecte_data)
        if respons_to_serv:
            return self.stat.card_update 
        return self.stat.card_not_update
        
    def card_delete(self, data: dict) -> dict:
        """For delete a card."""
        title = data["title"]
        board = data["board"]
        response_db = self.req_DB.request_title_board(title, board)
        if not response_db:
            return self.stat.card_not_exist
        response_db_card_delete = self.req_DB.request_card_delete(title, board)
        if response_db_card_delete:
            return self.stat.card_delete 
        return self.stat.card_not_delete

    def column_info(self, data: dict) -> dict:
        """The column report. Getting info about a task."""
        board = data["board"]
        column = data["column"]
        assignee = data["assignee"]
        response_db = self.req_DB.request_info_column(board, column, assignee)
        self.obj_estim1 = Estimation('0h')
        if not response_db:
            return self.stat.colum_not_info
        response_to_serv = {
                            "board": board,
                            "column": column,
                            "assignee": assignee,
                            "count": len(response_db),
                            "estimation": None,
                            "cards": []
                            }
        for card in response_db:
            card_dict = {
                        "title": card[0],
                        "board": card[1],
                        "status": card[2],
                        "description": card[3],
                        "assignee": card[4], 
                        "estimation": card[5], 
                        "created_at": str(datetime.fromtimestamp(int(card[6]))),
                        "created_by": card[7],
                        "last_updated_at": str(datetime.fromtimestamp(int(card[8]))),
                        "last_updated_by": card[9]
                        }
            response_to_serv["cards"].append(card_dict)
            obj_estim2 = Estimation(card[5])
            self.obj_estim1 += obj_estim2
        obj_sum_estim = SumEstimation(self.obj_estim1)  
        response_to_serv["estimation"] = obj_sum_estim.response 
        return response_to_serv


class Estimation:
    """The class calculating some estimations in the month,
     week, day, hour format and formatting them to the hour format.

     """
    def __init__(self, value):
        self.value_str = value
        self.val_hour = self.pars_transfor(value)

    def __str__(self):
        return self.value_str

    def __repr__(self):
        return self.value_str

    def pars_transfor(self, value: str) -> int:
        """The function formatting 'value' to the number to the hour format."""
        char = str(value[-1])
        numer = int(value[:-1])
        if char == 'm':
            return numer * 160
        if char == 'w':
            return numer * 40
        if char == 'd':
            return numer * 8
        if char == 'h':
            return numer

    def __add__(self, other):
        instance = str(int(other.val_hour) + int(self.val_hour)) + 'h'
        return Estimation(instance)

class SumEstimation:
    """The class for calculation the sum of ratings
     for all tasks assigned to the performer in this column.

     """
    def __init__(self, odb_estim):
        self.response = ""
        self.val_hour = int(str(odb_estim)[:-1])
        self.month(self.val_hour)

    def month(self, value):
        """The processing of months."""
        int_part = value // 160
        if int_part:
            self.response += f"{int_part}m"
            remain = value % 160 
            self.week(remain)
            return
        self.week(value)  

    def week(self, value):
        """The processing of weeks."""
        int_part = value // 40
        if int_part:
            self.response += f"{int_part}w"
            remain = value % 40
            self.day(remain)
            return
        self.day(value)

    def day(self, value):
        """The processing of days."""
        int_part = value // 8
        if int_part:
            self.response += f"{int_part}d"
            remain = value % 8
            self.hour(remain)
            return
        self.hour(value)

    def hour(self, value):
        """The processing of hours."""
        if value:
            self.response += f"{value}h"
