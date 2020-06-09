from flask import Flask, request
from logic import UsingDB
from logic import Statuses
import psycopg2

app = Flask(__name__)

def authentific(headers):
    username = str(request.headers['UserName'])
    usersecret = str(request.headers['UserSecret'])
    autenf_data = (username, usersecret)
    if UsingDB().autefication_users(autenf_data):
        print('Аутенфикация пройдена')
        return True
    print('Аутенфикация НЕ пройдена')
    return False

@app.route("/api/v1/user/list", methods=['POST'])
def get_all_users():
    """ Get all users."""
    if authentific(request.headers):
        response = UsingDB().get_all_users()
        print(response)
        return response
    return Statuses().aut_error

@app.route("/api/v1/board/create", methods=['POST'])
def board_create():
    """ For create a snew board."""
    if authentific(request.headers):
        data = request.json
        username = str(request.headers['UserName'])
        reponse = UsingDB().create_board(data, username)
        print(reponse)
        return reponse
    return Statuses().aut_error

@app.route("/api/v1/board/delete", methods=['POST'])
def board_delete():
    """ For delete board."""
    if authentific(request.headers):
        data = request.json
        return UsingDB().delete_board(data)
    return Statuses().aut_error

@app.route("/api/v1/board/list", methods=['POST'])
def board_list():
    """ Get all boards."""
    if authentific(request.headers):
        return UsingDB().get_all_boars()
    return Statuses().aut_error

@app.route("/api/v1/card/create", methods=['POST'])
def card_create():
    """ For cread a new card."""
    if authentific(request.headers):
        username = str(request.headers['UserName'])
        data = request.json
        return UsingDB().create_cards(data, username)
    return Statuses().aut_error

@app.route("/api/v1/card/update", methods=['POST'])
def card_update():
    """ For update a card"""
    if authentific(request.headers):
        username = str(request.headers['UserName'])
        data = request.json
        response = UsingDB().update_card(data, username)
        print(response)
        return response
    return Statuses().aut_error

@app.route("/api/v1/card/delete", methods=['POST'])
def card_delete():
    """ For delete a card"""
    if authentific(request.headers):
        data = request.json
        response = UsingDB().card_delete(data)
        print(response)
        return response
    return Statuses().aut_error

@app.route("/api/v1/report/cards_by_column", methods=['POST'])
def colum_info():
    """ Get info about a task"""
    if authentific(request.headers):
        data = request.json
        response = UsingDB().column_info(data)
        print(response)
        return response
    return Statuses().aut_error


if __name__ == "__main__":
    app.run()
