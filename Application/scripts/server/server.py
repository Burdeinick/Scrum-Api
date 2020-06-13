from flask import Flask, request
from scripts.logic.logic import UsingDB
from scripts.logic.logic import Statuses
import psycopg2


app = Flask(__name__)


def authentific(headers: dict) -> bool:
    """This function for authentification of user."""
    try:
        username = request.headers['UserName']
        usersecret = request.headers['UserSecret']
        autenf_data = (username, usersecret)
    except KeyError:
        print("Error: invalid request form 'UserName' or 'UserSecret'.")
        return False
    if UsingDB().autefication_users(autenf_data):
        print(f"Пользователь '{username}' прошел аутентификацию.")
        return True
    print(f"Пользователь '{username}' не прошел аутентификацию.")
    return False


@app.route("/api/v1/user/list", methods=['POST'])
def get_all_users() -> dict:
    """Get all users."""
    if authentific(request.headers):
        response = UsingDB().get_all_users()
        print(response)
        return response
    return Statuses().aut_error


@app.route("/api/v1/board/create", methods=['POST'])
def board_create() -> dict:
    """For create a snew board."""
    if authentific(request.headers):
        data = request.json
        head = request.headers
        reponse = UsingDB().create_board(data, head)
        print(reponse)
        return reponse
    return Statuses().aut_error


@app.route("/api/v1/board/delete", methods=['POST'])
def board_delete() -> dict:
    """For delete board."""
    if authentific(request.headers):
        data = request.json
        response = UsingDB().delete_board(data)
        print(response)
        return response
    return Statuses().aut_error


@app.route("/api/v1/board/list", methods=['POST'])
def board_list() -> dict:
    """Get all boards."""
    if authentific(request.headers):
        response = UsingDB().get_all_boars()
        print(response)
        return response
    return Statuses().aut_error


@app.route("/api/v1/card/create", methods=['POST'])
def card_create() -> dict:
    """For cread a new card."""
    if authentific(request.headers):
        data = request.json
        head = request.headers
        response = UsingDB().create_cards(data, head)
        print(response)
        return UsingDB().create_cards(data, head)
    return Statuses().aut_error


@app.route("/api/v1/card/update", methods=['POST'])
def card_update() -> dict:
    """For update a card."""
    if authentific(request.headers):
        data = request.json
        head = request.headers
        response = UsingDB().update_card(data, head)
        print(response)
        return response
    return Statuses().aut_error


@app.route("/api/v1/card/delete", methods=['POST'])
def card_delete() -> dict:
    """For delete a card."""
    if authentific(request.headers):
        data = request.json
        response = UsingDB().card_delete(data)
        print(response)
        return response
    return Statuses().aut_error


@app.route("/api/v1/report/cards_by_column", methods=['POST'])
def colum_info() -> dict:
    """Get info about a task."""
    if authentific(request.headers):
        data = request.json
        response = UsingDB().column_info(data)
        print(response)
        return response
    return Statuses().aut_error

