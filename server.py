from flask import Flask, request
from logic import UsingDB
import psycopg2
app = Flask(__name__)


@app.route("/api/v1/user/list", methods=['POST'])
def get_all_users():
    """ Get all users"""
    username = request.headers['UserName']
    usersecret = request.headers['UserSecret']
    autenf_data = (username, usersecret)
    us_db = UsingDB()

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена', us_db.get_all_users())
        return us_db.get_all_users()

    else:
        print({'Authentification': 'Error'})
        return {'Authentification': 'Error'}
        














@app.route("/api/v1/board/create", methods=['POST'])
def board_create():
    """ For create a snew board"""
    username = request.headers['UserName']
    usersecret = request.headers['UserSecret']
    autenf_data = (username, usersecret)
    data = request.json
    us_db = UsingDB()

    if us_db.autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        us_db.create_new_board(data, username)
        return({'Status': 'A board was created'})
    else:
        print({'Authentification': 'Error'})
        return {'Authentification': 'Error'}






















@app.route("/api/v1/board/delete", methods=['POST'])
def board_delete():
    """ For delete board"""
    print(request.json)
    return 'Ok'

@app.route("/api/v1/board/list", methods=['POST'])
def board_list():
    """ Get all boards"""
    print(request.headers)
    return 'ok'

@app.route("/api/v1/card/create", methods=['POST'])
def card_create():
    """ For cread a new card"""
    print(request.json)
    return 'Ok'

@app.route("/api/v1/card/update", methods=['POST'])
def card_update():
    """ For update a card"""
    print(request.json)
    return 'Ok'

@app.route("/api/v1/card/delete", methods=['POST'])
def card_delete():
    """ For delete a card"""
    print(request.json)
    return 'Ok'

@app.route("/api/v1/report/cards_by_column", methods=['POST'])
def colum_info():
    """ Get info about a task"""
    print(request.json)
    return 'Ok'


if __name__ == "__main__":
    app.run()
