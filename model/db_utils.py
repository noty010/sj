#Run 'CREATE DATABASE tccsj' in MySQL Workbench before running setup.py

def setup(cnx): # Inicializa o banco de dados para rodar a API
    def parse(cmdlist, file): # Lê os comandos em MySQL e executa
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

def getobjects(cnx, table, cod=None): # Busca objetos de uma tabela
    def assignobjects(rows, table):
        results = []
        cursor.execute("SHOW COLUMNS FROM %s" % table)
        columns = [row[0] for row in cursor.fetchall()]
        for row in rows:
            results.append({
                for i in range(len(columns)):
                    columns[i] = row[i]
            })
        cursor.close()

    cursor = cnx.cursor()
    if cod is None:
        cursor.execute("SELECT * FROM" % table)
        rows = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM %s WHERE cod = %i" % (table, cod))
        rows = cursor.fetchall()
    assignobjects(rows, table)