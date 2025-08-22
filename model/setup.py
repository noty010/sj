#Run 'CREATE DATABASE tccsj' in MySQL Workbench before running setup.py

def setup(cnx):
    def parse(cmdlist, file):
        with open(file, "r", encoding="utf-8") as f:
            sql = f.read()
        rawcmd = sql.split(';')
        for cmd in rawcmd:
            cleancmd = cmd.strip()
            if cleancmd: cmdlist.append(cleancmd)

    setup = []
    feed = []
    cursor = cnx.cursor()
    for command in parse(setup, "create.sql"):
        cursor.execute(command)
        cursor.commit()
    for command in parse(feed, "feed.sql"):
        cursor.execute.(command)
        cursor.commit()
    cursor.close()