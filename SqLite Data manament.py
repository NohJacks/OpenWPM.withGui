import sqlite3
from sqlite3 import Error

def create_connection(database_file):
    """ create a database connection to the SQLite database
            specified by the db_file
        :param database_file: database file
        :return: Connection object or None
        """
    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e)

    return conn


def  extract_javascript_cookies(conn):
    cur = conn.cursor()
    cur.execute('Select script_url from javascript')

    rows = cur.fetchall()

    with open("compare.txt", "w+", encoding="utf8") as files:
        for row in rows:
            files.write(row[0] +  "\n")

def main():
    #database = r"/home/ryan/PycharmProjects/OpenWPM.withGui/datadir/crawl-data.sqlite"
    database = "/home/ryan/PycharmProjects/OpenWPM.withGui/datadir/crawl-data.sqlite"

    # create a database connection
    conn = sqlite3.connect(database)
    cursor = conn.execute("PRAGMA table_info(mytable);")
    results = cursor.fetchall()
    print(results)

    with conn:
        print("JavaScript Cookies")
        extract_javascript_cookies(conn)

if __name__=='__main__':
    main()