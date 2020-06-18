import unittest
import sys
import json
sys.path.insert(0, 'Application')
from scripts.server.server import app


class TestApi(unittest.TestCase):
    """This class for the testing of Api.

    The checking the interaction of client requests and server responses.

    """
    def test_1_get_all_users(self):
        """Test. It must get all the users."""
        x = (
            ({"UserName": "Kop", "UserSecret": "456"}, ({'users': [{'username': 'Kop'}]})),
            ({"UserNam": "Kop", "UserSecret": "456"}, ({"status": "Authentification Error."})),
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
        """Test. The creation of a board."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({"title": 'New board',
                    "columns": [
                                "ToDo",
                                "InProgress",
                                "Done"
                                ]
                  }, {"status": "The board is created."}
                 ),

                ({"itle": 'New board',
                    "columns": [
                                "ToDo",
                                "InProgress",
                                "Done"
                                ]
                  }, {"status": "Invalid request form 'data' of client."}
                 ),

            ({"title": 'New board',
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
        """Test. Get all boards."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        with app.test_client() as client:
            request = client.post('api/v1/board/list', headers=headers)
            resp_dict = {'count': None}
            resp_dict['count'] = request.json['count']
            self.assertEqual(resp_dict, {'count': '1'})

    def test_4_card_create(self):
        """Test. The creation test of a new card.
        
        The problem in logic: if "status","description","assignee",
        "Username", "estimation" will have the mistakes of key,
        in this case they have not updated!!!

        """
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4w"
                    }, {"status": "The card is created."}
                 ),
                ({
                    "itle": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4w"
                    }, {"status": "Invalid request form 'data' of client."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "Не известная доска",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4w"
                    }, {"status": "The new card was don't created, such board no exist."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4w"
                    }, {"status": "This a card already exist at this board."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4"
                    }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4hd"
                    }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}
                 ),
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/card/create', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_5_update_card(self):
        """Test. The creation test of a new card.The update test of a new card."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "ToDo",
                  }, {"status": "The card has updated."}
                 ),
                ({
                    "title": "Card 1",
                    "oard": "New board",
                    "status": "ToDo",
                  }, {"status": "Invalid request form 'data' of client."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "ToDo",
                    "description": "New description",
                    "assignee": "Username",
                    "estimation": "7w"
                  }, {"status": "The card has updated."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "ToDo",
                    "description": "New description",
                    "assignee": "Username",
                    "estimation": "7P"
                  }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "Такой доски нет",
                    "status": "ToDo",
                  }, {"status": "The 'Board' and the 'title' have not match."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4hd"
                  }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "414"
                  }, {"status": "Invalid 'estimation'. Please repair the field 'estimation'."}
                 ),
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/card/update', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_6_column_info(self):
        """Test. Этот отчет позволяет получить информацию о задачах, которые находятся в определенной
        колонке.

        """
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({
                    "oard": "New board",
                    "column": "ToDo",
                    "assignee": "Username"
                  }, {"status": "Invalid request form 'data' of client."}
                 ),
                ({
                    "board": "New board",
                    "column": "ToDo",
                    "assignee": "Other name"
                  }, {"status": "The information about these columns are absent."}
                 )
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/report/cards_by_column', headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)
        data = {
                "board": "New board",
                "column": "ToDo",
                "assignee": "Username"
                }
        with app.test_client() as client:
            request = client.post('api/v1/report/cards_by_column', headers=headers, json=data)
            resp_dict = {'assignee': request.json['assignee'], 'board': request.json['board']}
            self.assertEqual(resp_dict, {'assignee': 'Username', 'board': 'New board'})

    def test_7_card_delete(self):
        """Test. The creation test of a new card.The test of remove the card."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({
                    "itle": "Card 1",
                    "board": "New board"
                  }, {"status": "Invalid request form 'data' of client."}
                 ),
                ({
                    "title": "Some kind of card",
                    "board": "New board"
                  }, {"status": "The card does not exist."}
                 ),
                ({
                    "title": "Card 1",
                    "board": "New board"
                  }, {"status": "The card is removed."}
                 )
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/card/delete',  headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)

    def test_8_board_delete(self):
        """Test. The creation test of a new card.The test of remove the board."""
        headers = {"UserName": "Kop", "UserSecret": "456"}
        x = (
                ({"tle": "New board"}, {"status": "Invalid request form 'data' of client."}),
                ({"title": "Some kind of Board"}, {"status": "This a board does not exist."}),
                ({"title": "New board"}, {"status": "The board is removed."})
            )
        for value in x:
            data, extended = value
            with app.test_client() as client:
                request = client.post('api/v1/board/delete',  headers=headers, json=data)
                with self.subTest(x=value):
                    self.assertEqual(request.json, extended)


def test_server_run():
    unittest.main()

test_server_run()
