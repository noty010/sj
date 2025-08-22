#Run 'CREATE DATABASE tccsj' in MySQL Workbench before running setup.py

import mysql.connector

cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'aluno',
    database = 'tccsj'
)

setup = []
feed = []

def parse(cmdlist, file):
    with open(file, "r", encoding="utf-8") as f:
        sql = f.read()
    rawcmd = sql.split(';')
    for cmd in rawcmd:
        cleancmd = cmd.strip()
        if cleancmd:
            cmdlist.append(cleancmd)

def setup():
    cursor = cnx.cursro()
    for command in parse(setup, "database/setup.sql"):
        cursor.execute(command)
        cursor.commit()
    for command in parse(feed, "database/feed.sql"):
        cursor.execute.(command)
        cursor.commit()
    cursor.close()

setup()