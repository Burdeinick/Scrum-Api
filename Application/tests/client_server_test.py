import unittest
import sys
sys.path.insert(0, 'Application')
from scripts.server.server import app
import json


class TestApi(unittest.TestCase):
    """ """
    def test_1_get_all_users(self):
        """It must get all the users."""
        headers_1 = {"UserName": "Kop", "UserSecret": "456"}
        headers_2 = {"UserNam": "Kop", "UserSecret": "456"}
        with app.test_client() as client:
            result_1 = client.post('api/v1/user/list', headers=headers_1)
            self.assertEqual(result_1.json, {'users': [{'username': 'Kop'}]})
            result_2 = client.post('api/v1/user/list', headers=headers_2)
            self.assertEqual(result_2.json, {"status":"Authentification Error."})


    
    # def test_2_get_all_users(self):
    #     """It must get all the users."""
    #     headers = {"UserNam": "Kop", "UserSecret": "456"}
    #     with app.test_client() as client:
    #         result = client.post('api/v1/user/list', headers=headers)
    #         self.assertEqual(result.json, {"status":"Authentification Error."})




    # def test_2_board_create(self):
    #     """The creation of the Board."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {
    #             "title": 'Новая доска',
    #             "columns": [
    #                         "ToDo",
    #                         "InProgress",
    #                         "Done"
    #                         ]
    #             }
    #     with app.test_client() as client:
    #         result = client.post('api/v1/board/create', headers=headers, json=data)
    #         self.assertEqual(result.json, {"status": "The board is created."})

    # def test_3_board_list(self):
    #     """Get all boards."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     with app.test_client() as client:
    #         result = client.post('api/v1/board/list', headers=headers)
    #         resp_dict = {'count': None}
    #         resp_dict['count'] = result.json['count']
    #         self.assertEqual(resp_dict, {'count': '1'})

    # def test_4_card_create(self):
    #     """ """
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {
    #             "title": "Карточка 1",
    #             "board": "Новая доска",
    #             "status": "Noooo",
    #             "description": "Необходимо проверить",
    #             "assignee": "Username",
    #             "estimation": "4w"
    #         }
    #     with app.test_client() as client:
    #         result = client.post('api/v1/card/create', headers=headers, json=data)
    #         self.assertEqual(result.json, {"status": "The card is created."})

    # def test_5_update_card(self):
    #     """The test of update the card."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {
    #             "title": "Карточка 1",
    #             "board": "Новая доска",
    #             "status": "ToDo",
    #             }
    #     with app.test_client() as client:
    #         result = client.post('api/v1/card/update',  headers=headers, json=data)
    #         self.assertEqual(result.json, {"status": "The card has updated."})

    # def test_6_column_info(self):
    #     """The test of update the card."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {
    #         "board": "Новая доска",
    #         "column": "ToDo",
    #         "assignee": "Username"
    #         }
    #     with app.test_client() as client:
    #         result = client.post('api/v1/report/cards_by_column',  headers=headers, json=data)
    #         resp_dict = {'assignee': None, 'board': None}
    #         resp_dict['assignee'] = result.json['assignee']
    #         resp_dict['board'] = result.json['board']
    #         self.assertEqual(resp_dict, {'assignee': 'Username', 'board': 'Новая доска'})

    # def test_7_card_delete(self):
    #     """The test of remove the card."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {
    #             "title": "Карточка 1",
    #             "board": "Новая доска"
    #             }
    #     with app.test_client() as client:
    #         result = client.post('api/v1/card/delete',  headers=headers, json=data)
    #         self.assertEqual(result.json, {"status": "The card is removed."})

    # def test_8_board_delete(self):
    #     """The test of remove the board."""
    #     headers = {"UserName": "Kop", "UserSecret": "456"}
    #     data = {"title": "Новая доска"}
    #     with app.test_client() as client:
    #         result = client.post('api/v1/board/delete',  headers=headers, json=data)
    #         self.assertEqual(result.json, {"status": "The board is removed."})




def test_server_run():
    unittest.main()

test_server_run()