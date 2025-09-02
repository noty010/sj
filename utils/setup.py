def setup(cnx):
    setup = []
    feed = []
    cursor = cnx.cursor()
    for command in parse(setup, "create.sql"):
        cursor.execute(command)
        cursor.commit()
    cursor.close()