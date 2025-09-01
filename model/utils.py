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

def getall(cnx, table):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM %s" % table)
    results = cursor.fetchall()
    cursor.close()
    return results

def getbyid(cnx, table, code):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM %s WHERE cod = %i" % (table, code))
    results = cursor.fetchall()
    cursor.close()
    return results

def delete(cnx, table, code):
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM %s WHERE cod = %i" % (table, code))
    cursor.commit()
    cursor.close()