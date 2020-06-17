# Scrum Api

The backend application for managing tasks, on the Scrum methodology.

## What is Scrum Api?
Scrum Api is a backend for a small app
task management, which, can be used on the Scrum methodology.
The task cards are placed on the Board and can move through the columns changing their status.
For task, you can assign a responsible person who will perform this task of a certain time.
You can build reports on tasks, how many tasks are planned, how many are in progress, and how many completed.

For manage boards and tasks, you must use POST requests to the server.
All api methods have a prefix: http://your_host:your_port/api/v1/your_request.
The POST request headers are passed for all api methods: UserName - name of the user, UserSecret - token of the user.

* At all of prosperous requests will returning of data json or other the positive answers. Example: {"status": "The board is created."}
* If the result is negative. For example:  {"status": "The card does not exist."}
* In case of an identification error: {"status": "Authentification Error."}
  
  



## Getting Started
1. Install all dependencies $ pip install -r requirements.txt
2. Start the database server PostgreSQL.
3. In the file config.json fill in the parameters of the database and server:
    
       {
        "server": {"host": "...", 
                    "port": "..."}, 
        "Data_Base": {"dbname": "...", 
                        "user": "...",
                        "password": "..."}
        }

After that, the server will be started and the api is ready to work.


