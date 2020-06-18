build :
	python3 Application/tests/preparing_db_test.py

test :
	python3 Application/tests/client_server_test.py

run :
	python3 Application/main.py