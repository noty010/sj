from ..model.utils import setup, feed, getall, getbyid, delete
from flask import Flask, make_response, jsonify, render_template
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'aluno',
    database = 'tccsj'
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)