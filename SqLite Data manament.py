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

def select_task_by_priority(conn,priority):
    """
       Query tasks by priority
       :param conn: the Connection object
       :param priority:
       :return:
       """
    cur = conn.cursor()
    cur.execute("SElect * from tasks WHere Priority=?",(priority))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority")
        select_task_by_priority(conn, 1)

        print("2. Query ALL task ")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()