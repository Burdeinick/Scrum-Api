# Scrum Api

The backend application for managing tasks, on the Scrum methodology.

## What is Scrum Api?
Scrum Api is a backend for a small app
task management, which, can be used on the Scrum methodology.
The task cards are placed on the Board and can move through the columns changing their status.
For task, you can assign a responsible person who will perform this task of a certain time.
You can build reports on tasks, how many tasks are planned, how many are in progress, and how many completed.

For manage boards and tasks, you must use POST requests to the server.
All api methods have a prefix: `http://your_host:your_port/api/v1/your_request`.

The POST request headers are passed for all api methods: UserName - name of the user, UserSecret - token of the user.

* At all of prosperous requests will returning of data json or other the positive answers. For example: `{"status": "The board is created."}`
* If the result is negative. For example: `{"status": "The card does not exist."}`
* In case of an identification error: `{"status": "Authentification Error."}`
  
## Getting Started

1. Install all dependencies `$ pip install -r requirements.txt`
2. Start the database server PostgreSQL.
3. In the file config.json fill in the parameters of the database and server:
    
       {
        "server": {"host": "...", 
                    "port": "..."}, 
        "Data_Base": {"dbname": "...", 
                        "user": "...",
                        "password": "..."}
        }
4. Run these commands in bash:

        $ make build
        $ make test
        $ make run

After that, the server will be started and the api is ready to work.

## Example of interaction with API
In the DB has default one user for testing API: 
- `"UserName": "Kop"`, 
- `"UserSecret": "456"`

### The list of user:
It's the example request:

        def get_users():
            url = r'http://127.0.0.1:5000/api/v1/user/list'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            requests.post(url, headers=headers)

### Create a board:
- title - this is the name of the Board that the user will see. Required field
- columns - this is a list of columns on the Board that the task cards will move through.
Required field

It's the example request:

        def board_create():
            url = r'http://127.0.0.1:5000/api/v1/board/create'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {
                    "title": 'New board',
                    "columns": [
                                "ToDo",
                                "InProgress",
                                "Done"
                                ]
                    }
            requests.post(url, json=data, headers=headers)

### To remove a board:
It's the example request:

        def board_delete():
            url = r'http://127.0.0.1:5000/api/v1/board/delete'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {"title": "New board"}
            requests.post(url, json=data, headers=headers)


### Show all the boards:

It's the example request:

        def board_list():
            url = r'http://127.0.0.1:5000/api/v1/board/list'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            requests.post(url, headers=headers)

### Create a card:

- title - name of the card that the user will see. Required field.
- board - the board to place the card on. Required field.
- status - the status of the task and the column where the task is located on the board. Required field.
- description-detailed text of the issue. Required field.
- assignee - the user to whom the task is assigned. Required field.
- estimation - estimation of labor costs for the task in ideal units. Required field. 
  
  Tasks are evaluated in ideal time units:
  - h - ideal working hour
  - d - perfect working day. Equal to 8 ideal working hours.
  - w - is the ideal work week. Equal to 5 ideal working days.
  - m - is an ideal working month. Equal to 4 ideal working weeks.
  

It's the example request:

        def card_create():
            url = r'http://127.0.0.1:5000/api/v1/card/create'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {
                    "title": "Card 1",
                    "board": "New board",
                    "status": "Noooo",
                    "description": "Need to check",
                    "assignee": "Username",
                    "estimation": "4w"
                    }
            requests.post(url, json=data, headers=headers) 

### Update a card:

It's the example request:

        def card_update():
            url = r'http://127.0.0.1:5000/api/v1/card/update'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {
                    "title": "Card 1",
                    "board": "New board",
                    "status": "ToDo",
                    }
            requests.post(url, json=data, headers=headers) 

### Delete a card:

It's the example request:

        def card_delete():
            url = r'http://127.0.0.1:5000/api/v1/card/delete'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {
                    "title": "Card 1",
                    "board": "New board"
                  }
            requests.post(url, json=data, headers=headers) 

### Column report:

It's the example request:

        def colum_info():
            url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
            headers = {"UserName": "Kop", "UserSecret": "456"}
            data = {
                    "board": "New board",
                    "column": "ToDo",
                    "assignee": "Other name"
                    }
            requests.post(url, json=data, headers=headers) 
