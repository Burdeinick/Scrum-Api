import json
from scripts.server.server import app


def main():
    app.run(*get_config())

def get_config():
    with open('config.json') as config:
        json_str = config.read()
        json_str = json.loads(json_str)

    host = json_str['server']['host']
    port = json_str['server']['port']
    return host, port


if __name__ == "__main__":
    main()
