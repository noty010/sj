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
    cursor = cnx.cursor()
    if cod is None:
        cursor.execute("SELECT * FROM" % table)
        objects = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM %s WHERE cod = %i" % (table, cod))
        objects = cursor.fetchall()
    cursor.close()