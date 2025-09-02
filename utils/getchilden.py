def getchildren(cnx, table, code):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f'SELECT cod, nome FROM {table} WHERE fk = {code}')
    results = cursor.fetchall()
    return results