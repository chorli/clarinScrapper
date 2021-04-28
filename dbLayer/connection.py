import sqlite3
from datetime import datetime

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print("error", e)

    return conn

def checkIfNoticeHasBeenImported(sourceId, notice, conn):
    cur = conn.cursor()
    sql = "SELECT EXISTS(SELECT 1 FROM Notices WHERE SourceId =" + str(sourceId) + " AND Header='" + notice.header + "' AND Contents='" + notice.contents + "')";
    exists = cur.execute(sql).fetchone()[0]
    
    return exists

def insertNewNotice(notice, conn):
    cur = conn.cursor()
    sql = "INSERT INTO Notices (SourceId, Header, Contents, DateCreated, DateUpdated) VALUES (?, ?, ?, ?, ?)"
    dateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    val = (1, notice.header, notice.contents, dateTime, dateTime)
    cur.execute(sql, val)

    conn.commit()

    return cur.rowcount