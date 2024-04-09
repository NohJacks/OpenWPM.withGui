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

def select_all_tasks(conn):
    """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
    cur = conn.cursor()
    cur.execute("select * from tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def  extract_javascript_cookies(conn):
    cur = conn.cursor()
    cur.execute('Select * from javascript')

    rows = cur.fetchall()

    for row in rows:
        print(row)

        #lis=len(row)

    file_path = "compare.txt"
    with open("compare.txt", encoding="utf8") as files:
        pass
        #files.write(lis)
    print(f"File '{file_path}' created successfully.")


"""    print("finding all. ANYTHING AND EVERYTHING AND ALL OF THE TIME")
    cur.execute('Select * from javascript')
    rows = cur.fetchall()

    for row in rows:
        taxa = rows.select('table')[5:]

    print("printing taxa")
    print(taxa)"""


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
        extract_javascript_cookies(conn,1)

        print("2. Query ALL task ")
        select_all_tasks(conn)


if __name__=='__main__':
    main()