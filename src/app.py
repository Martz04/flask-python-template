from flask import Flask, request, json
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://root:S3cret@mongo")
todo_db = client["todo"]

today = todo_db["today"]


@app.route('/')
def hello_world():
    app.logger.debug("debug")
    app.logger.info("info")
    app.logger.error("error")
    return 'Hello World!'


@app.route('/todo', methods=['POST'])
def add_todo():
    payload = json.loads(request.data)
    app.logger.info(f"method=/todo, request_data={payload}")

    today.insert_one(payload)
    return json.dumps({
        "Message": "success"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001)
