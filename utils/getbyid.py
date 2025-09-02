def getbyid(cnx, table, code):
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {table} WHERE code = {code}')
    results = cursor.fetchall()
    cursor.close()
    return results