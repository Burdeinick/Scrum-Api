import requests


def get_users():
    """ For testing geting all users"""
    url = r'http://127.0.0.1:5000/api/v1/user/list'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    requests.post(url, headers=headers)


def board_create():
    """For board create"""
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "title": 'Новая доска',
            "columns": [
                        "ToDo",
                        "InProgress",
                        "Done"
                        ]
            }
    requests.post(url, json=data, headers=headers)


def board_delete():
    """ For board delete."""
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {"title": "Новая доска"}
    requests.post(url, json=data, headers=headers)


def board_list():
    """Get all boards."""
    url = r'http://127.0.0.1:5000/api/v1/board/list'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    requests.post(url, headers=headers)   


def card_create():
    """Create a card."""
    url = r'http://127.0.0.1:5000/api/v1/card/create'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
                "title": "Карточка 1",
                "board": "Новая доска",
                "status": "Noooo",
                "description": "Необходимо проверить",
                "assignee": "Username",
                "estimation": "4w"
            }
    requests.post(url, json=data, headers=headers) 


def card_update():
    """ For update a card"""
    url = r'http://127.0.0.1:5000/api/v1/card/update'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "title": "Тест снова 1",
            "board": "tre",
            "status": "обновил карту2",
            }
    requests.post(url, json=data, headers=headers) 


def card_delete():
    """For delete a card."""
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "title": "Тест снова 1",
            "board": "tre"
            }
    requests.post(url, json=data, headers=headers) 


def colum_info():
    """Get info about a task."""
    url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
    headers = {"UserName": "Kop", "UserSecret": "456"}
    data = {
            "board": "tre",
            "column": "Noooo",
            "assignee": "Username"
            }
    requests.post(url, json=data, headers=headers) 

# get_users()
# board_create()
# board_delete()
# board_list()
# card_create()
# card_update()
# card_delete()
# colum_info()
