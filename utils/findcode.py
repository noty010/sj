def findcode(cnx, table, handle):
    cursor = cnx.cursor()
    cursor.execute(f'SELECT code FROM {table} WHERE handle = {handle}')
    code = cursor.fetchall()
    return code