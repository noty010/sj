def delete(cnx, table, code):
    cursor = cnx.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE code = {code}')
    cursor.commit()
    cursor.close()