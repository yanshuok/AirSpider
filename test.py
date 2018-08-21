from datetime import datetime
from mysql import connector

def getConnection():
    return connector.connect(user='root', password='ys1234ys', database='bj_air')


def main():
    conn = getConnection()
    t = datetime.now()

    cursor = conn.cursor()
    cursor.execute('insert into test (time) VALUES (%s)', [t])
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':

    main()
