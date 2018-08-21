from mysql import connector

def getConnection():
    conn = connector.connect(user='root', password='ys1234ys', database='bj_air')
    return conn


def insertAirQaulity(airList):
    conn = getConnection()
    cursor = conn.cursor()
    sql = 'insert into airquality (co_0, co_iaqi, co, no2_0, no2_iaqi, no2, so2_0, so2_iaqi, so2, o3_0, o3_iaqi, o3, pm25_0, pm25_iaqi, pm25, pm10_0, pm10_iaqi, pm10, first, grade, aqi, date, station_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.executemany(sql, airList)
    if cursor.rowcount<35:
        print('mysql dead')
    conn.commit()
    conn.close()
    cursor.close()


def getStationIds():
    conn = getConnection()
    cursor = conn.cursor()
    sql = 'select id from airquality_station'
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values