import json
import os

import pymysql as pymy

from flask import Flask, request
from pymysql.cursors import DictCursor as dc
from contextlib import closing

app = Flask(__name__)
conn = pymy.connect(host="database",
                    user="root",
                    password=os.environ['MYSQL_PASSWORD'],
                    db=os.environ['MYSQL_DATABASE'],
                    charset="utf8mb4",
                    cursorclass=dc)


@app.route('/')
def index():
    db_respose = []
    with closing(conn.cursor()) as cursor:
        query = "select * from feedbacks;"
        cursor.execute(query)
        for row in cursor:
            db_respose.append(row)
    return json.dumps(db_respose)


@app.route("/write_db", methods=["POST"])
def write():
    request_ip = request.remote_addr
    point = request.values.get("point")
    with closing(conn.cursor()) as cursor:
        cursor.execute(
            f"INSERT INTO feedbacks (ip, feedback) VALUES ('{request_ip}','{point}')")
    return json.dumps({"status_code": "200"}), {'Access-Control-Allow-Origin': '*'}


@app.route("/search_ip", methods=["POST", "GET"])
def search():
    db_respose = []
    request_ip = request.remote_addr
    with closing(conn.cursor()) as cursor:
        query = "select * from feedbacks;"
        cursor.execute(query)
        for row in cursor:
            db_respose.append(row.get("ip"))
    return json.dumps({"result": "true" if request_ip in db_respose else "false"}), {'Access-Control-Allow-Origin': '*'}


@app.route("/ping/")
def pong():
    return "pong"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port="5000")
