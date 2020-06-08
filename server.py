from flask import Flask, request
from logic import UsingDB
from logic import Statuses
import psycopg2
app = Flask(__name__)


@app.route("/api/v1/user/list", methods=['POST'])
def get_all_users():
    """ Get all users"""
    us_db = UsingDB()
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)

    if us_db.autefication_users(autenf_data):
        return us_db.get_all_users()
    else:
        print({'Authentification': 'Error'})
        return {'Authentification': 'Error'}

@app.route("/api/v1/board/create", methods=['POST'])
def board_create():
    """ For create a snew board"""
    us_db = UsingDB()
    statuses = Statuses()
    data = request.json
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)
    
    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return us_db.create_new_board(data, username)
    else:
        print({'Authentification': 'Error'})
        return statuses.authentif_error

@app.route("/api/v1/board/delete", methods=['POST'])
def board_delete():
    """ For delete board"""
    us_db = UsingDB()
    statuses = Statuses()
    data = request.json
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return us_db.delete_board(data)
    else:
        print({'Authentification': 'Error'})
        return statuses.authentif_error

@app.route("/api/v1/board/list", methods=['POST'])
def board_list():
    """ Get all boards"""
    us_db = UsingDB()
    statuses = Statuses()
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return us_db.get_all_boars()
        
    else:
        print({'Authentification': 'Error'})
        return statuses.authentif_error

@app.route("/api/v1/card/create", methods=['POST'])
def card_create():
    """ For cread a new card"""
    us_db = UsingDB()
    statuses = Statuses()
    data = request.json
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return us_db.create_new_cards(data, username)

    else:
        print({'Authentification': 'Error'})
        return statuses.authentif_error




























@app.route("/api/v1/card/update", methods=['POST'])
def card_update():
    """ For update a card"""
    us_db = UsingDB()
    statuses = Statuses()
    data = request.json
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return us_db.update_card(data, username)

    else:
        print({'Authentification': 'Error'})
        return statuses.authentif_error



























@app.route("/api/v1/card/delete", methods=['POST'])
def card_delete():
    """ For delete a card"""
    print( request.json)
    return 'Ok'

@app.route("/api/v1/report/cards_by_column", methods=['POST'])
def colum_info():
    """ Get info about a task"""
    print(request.json)
    return 'Ok'


if __name__ == "__main__":
    app.run()
