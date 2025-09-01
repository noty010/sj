def parse(cmdlist, file):
    with open(file, "r", encoding="utf-8") as f:
        sql = f.read()
    rawcmd = sql.split(';')
    for cmd in rawcmd:
        cleancmd = cmd.strip()
        if cleancmd: cmdlist.append(cleancmd)

def setup(cnx):
    setup = []
    feed = []
    cursor = cnx.cursor()
    for command in parse(setup, "create.sql"):
        cursor.execute(command)
        cursor.commit()
    cursor.close()

def feed(cnx):
    feed = []
    cursor = cnx.cursor()
    for command in parse(feed, "feed.sql"):
        cursor.execute(command)
        cursor.commit()
    cursor.close()

def findcode(cnx, table, handle):
    cursor = cnx.cursor()
    cursor.execute(f'SELECT code FROM {table} WHERE handle = {handle}')
    code = cursor.fetchall()
    return code

def getall(cnx, table):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {table}')
    results = cursor.fetchall()
    cursor.close()
    return results

def getbyid(cnx, table, code):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {table} WHERE code = {code}')
    results = cursor.fetchall()
    cursor.close()
    return results

def delete(cnx, table, code):
    cursor = cnx.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE code = {code}')
    cursor.commit()
    cursor.close()