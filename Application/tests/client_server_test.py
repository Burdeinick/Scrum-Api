import unittest
import sys
sys.path.insert(0, 'Application')
from scripts.server.server import app
import json


class TestApi(unittest.TestCase):
    """This class for the testing of logic."""
    def test_1_get_all_users(self):
        """It must get all the users."""
        x = (
            ({"UserName": "Kop", "UserSecret": "456"}, ({'users': [{'username': 'Kop'}]})),
            ({"UserNam": "Kop", "UserSecret": "456"}, ({"status":"Authentification Error."})),
            ({"UserName": "Kop", "serSecret": "456"}, ({"status": "Authentification Error."})),
            ({"": "Kop", "UserSecret": "456"}, ({"status": "Authentification Error."})),
            ({0: "Kop", "UserSecret": "456"}, ({"status": "Authentification Error."}))
            )
        for value in x:
            inp_headers, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/user/list', headers=inp_headers)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_2_board_create(self):
        """The creation of a board."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({"title": 'Новая доска',
                "columns": [
                            "ToDo",
                            "InProgress",
                            "Done"
                            ]
                }, {"status": "The board is created."}),

            ({"itle": 'Новая доска',
                "columns": [
                            "ToDo",
                            "InProgress",
                            "Done"
                            ]
                }, {"status": "Invalid request form 'data' of client."}),

            ({"title": 'Новая доска',
                "columns": [
                            "ToDo",
                            "InProgress",
                            "Done"
                            ]
                }, {'status': 'This a board already exist.'})

            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/board/create', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_3_board_list(self):
        """Test.Get all boards."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        with app.test_client() as client:
            result = client.post('api/v1/board/list', headers=headers)
            resp_dict = {'count': None}
            resp_dict['count'] = result.json['count']
            self.assertEqual(resp_dict, {'count': '1'})

    def test_4_card_create(self):
        """
        The creation test of a new card.

        The problem in logic: if "status","description","assignee",
        "Username", "estimation" will have the mistakes of key,
        in this case they have not updated!!!

        """
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "Noooo",
                "description": "Необходимо проверить",
                "assignee": "Username",
                "estimation": "4w"
                }, {"status": "The card is created."}),
            ({
                "itle": "Карточка 1",
                "board": "Новая доска",
                "status": "Noooo",
                "description": "Необходимо проверить",
                "assignee": "Username",
                "estimation": "4w"
                }, {"status": "Invalid request form 'data' of client."}),
            ({
                "title": "Карточка 1",
                "board": "Не известная доска",
                "status": "Noooo",
                "description": "Необходимо проверить",
                "assignee": "Username",
                "estimation": "4w"
                }, {"status": "The new card was don't created, such board no exist."}),
            ({
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "Noooo",
                "description": "Необходимо проверить",
                "assignee": "Username",
                "estimation": "4w"
                }, {"status": "This a card already exist at this board."})
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/card/create', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_5_update_card(self):
        """The update test of a new card."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "ToDo",
                }, {"status": "The card has updated."}),
            ({
                "title": "Карточка 1",
                "oard": "Новая доска",
                "status": "ToDo",
                }, {"status": "Invalid request form 'data' of client."}),
            ({
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "ToDo",
                "description": "New description",
                "assignee": "Username",
                "estimation": "7w"
                }, {"status": "The card has updated."}),
            ({
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "ToDo",
                "description": "New description",
                "assignee": "Username",
                "estimation": "7P"
                }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}),
            ({
                "title": "Карточка 1",
                "board": "Такой доски нет",
                "status": "ToDo",
                }, {"status": "The 'Board' and the 'title' have not match."})
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/card/update',headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_6_column_info(self):
        """Test. Этот отчет позволяет получить информацию о задачах, которые находятся в определенной
        колонке.
        
        """
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({
                "oard": "Новая доска",
                "column": "ToDo",
                "assignee": "Username"
            }, {"status": "Invalid request form 'data' of client."}),
            ({
                "board": "Новая доска",
                "column": "ToDo",
                "assignee": "Othet name"
                }, {"status": "The information about these columns are absent."})

            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/report/cards_by_column', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)
        data = {
                "board": "Новая доска",
                "column": "ToDo",
                "assignee": "Username"
                }
        with app.test_client() as client:
            result = client.post('api/v1/report/cards_by_column', headers=headers, json=data)
            resp_dict = {'assignee': result.json['assignee'], 'board': result.json['board']}
            self.assertEqual(resp_dict, {'assignee': 'Username', 'board': 'Новая доска'})

    def test_7_card_delete(self):
        """The test of remove the card."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({
                "itle": "Карточка 1",
                "board": "Новая доска"
                }, {"status": "Invalid request form 'data' of client."}),
            ({
                "title": "Какая-то карточка",
                "board": "Новая доска"
                }, {"status": "The card does not exist."}),
            
            ({
                "title": "Карточка 1",
                "board": "Новая доска"
                }, {"status": "The card is removed."})
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                response = client.post('api/v1/card/delete',  headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(response.json, extended)

    def test_8_board_delete(self):
        """The test of remove the board."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
            ({"tle": "Новая доска"}, {"status": "Invalid request form 'data' of client."}),
            ({"title": "Какая-то доска"}, {"status": "This a board does not exist."}),
            ({"title": "Новая доска"}, {"status": "The board is removed."} )
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                response = client.post('api/v1/board/delete',  headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(response.json, extended)


def test_server_run():
    unittest.main()

test_server_run()