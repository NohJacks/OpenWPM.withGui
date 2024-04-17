import sqlite3
import EasyListCompareScript
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


def extract_javascript_cookies(conn,filename):
    cur = conn.cursor()
    cur.execute('Select script_url from javascript')

    rows = cur.fetchall()

    datalist = []
    with open(filename, "w+", encoding="utf8") as files:
        for row in rows:
            files.write(row[0] +  "\n")
            datalist.append(row[0])
    return datalist

def main(filename):
    #database = r"/home/ryan/PycharmProjects/OpenWPM.withGui/datadir/crawl-data.sqlite"
    database = "./datadir/{}.sqlite".format(filename)

    # create a database connection
    conn = create_connection(database)
    #cursor = conn.execute("PRAGMA table_info(mytable);")
    #results = cursor.fetchall()
    #print(results)

    with conn:
        print("JavaScript Cookies")
        datalist = extract_javascript_cookies(conn, filename)
        comparator = EasyListCompareScript.CookieComparator('test1')
        comparator.setDatalist(datalist)
        comparator.compare()


if __name__=='__main__':
    pass

