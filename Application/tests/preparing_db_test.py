import psycopg2
import sys
sys.path.insert(0, 'Application/scripts')
from logic.logic import ConnectionDB


connect_db = ConnectionDB()
dbname, user, password = connect_db.get_config_db()


def create_users():
    with psycopg2.connect(dbname=dbname, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            request = """CREATE TABLE users
                        (
                            user_Id SERIAL PRIMARY KEY,
                            username varchar(70),
                            password varchar(70)     
                        )"""
            cursor.execute(request)
            conn.commit()


def create_boards():
    with psycopg2.connect(dbname=dbname, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            request = """CREATE TABLE boards
                        (                                
                            board_Id SERIAL PRIMARY KEY,  
                            title varchar(70),             
                            columns varchar(70),           
                            created_at integer,            
                            created_by varchar(70),         
                            last_updated_at integer,     
                            last_updated_by varchar(70)          
                        )"""
            cursor.execute(request)
            conn.commit()


def create_cards():
    with psycopg2.connect(dbname=dbname, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            request = """CREATE TABLE cards
                        (
                            card_Id SERIAL PRIMARY KEY,
                            title varchar(70),
                            board  varchar(70),
                            status varchar(70),
                            description varchar(70),
                            assignee varchar(70),
                            estimation varchar(70),
                            created_at integer,
                            created_by varchar(70),
                            last_updated_at integer,
                            last_updated_by varchar(70)
                        )"""
            cursor.execute(request)
            conn.commit()


def add_user():
    with psycopg2.connect(dbname=dbname, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            request = "INSERT INTO users (username, password)   \
                        VALUES ('Kop', '456')"
            cursor.execute(request)
            conn.commit()


def main():
    create_users()
    create_boards()
    create_cards()
    add_user()
    print('Ok')

main()