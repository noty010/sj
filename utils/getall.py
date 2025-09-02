def getall(cnx, table):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {table}')
    results = cursor.fetchall()
    cursor.close()
    return results