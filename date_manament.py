import sqlite3
import EasyListCompareScript
from sqlite3 import Error


def create_connection(database_file):
    # her laves databasen connection til SQlite database

    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e) #test/debug

    return conn


def extract_javascript_cookies(conn,filename):
    """her bliver script_url fra javascript lavet og lagt in i datalist"""
    cur = conn.cursor()
    cur.execute('Select script_url from javascript')

    rows = cur.fetchall()

    datalist = []
    with open(filename, "w+", encoding="utf8") as files:
        for row in rows:
            files.write(row[0] +  "\n")
            datalist.append(row[0])
    return datalist

def main(filename): #starter her efter betterWMP

    """her bliver vejen til hvor datafilen skal definret"""
    database = "./datadir/{}.sqlite".format(filename)

    # her laves databasen connection til SQlite database
    conn = create_connection(database)


    with conn:
        print("Connection")

        datalist = extract_javascript_cookies(conn, filename)
        comparator = EasyListCompareScript.CookieComparator('test69')
        comparator.setDatalist(datalist)
        comparator.compare()


if __name__=='__main__':
    pass

