from parse import parse

def feed(cnx):
    feed = []
    cursor = cnx.cursor()
    for command in parse(feed, "feed.sql"):
        cursor.execute(command)
        cursor.commit()
    cursor.close()