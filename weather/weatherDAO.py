from mysql import connector


def getConnection():
    return connector.connect(user='root', password='ys1234ys', database='bj_air')


def getUrls():
    conn = getConnection()
    cursor = conn.cursor()
    sql = 'select id, href from weather_station'
    cursor.execute(sql)
    values = cursor.fetchall()
    if cursor.rowcount<15:
        print('mysql dead')
    conn.commit()
    cursor.close()
    conn.close()
    return values


def insertWeahter24h(weather24List):
    conn = getConnection()
    cursor = conn.cursor()
    sql = 'insert into weather24h (station_id, date, dur, temperature, humidity, rain, wind_force, wind_driection) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.executemany(sql, weather24List)
    conn.commit()
    cursor.close()
    conn.close()





