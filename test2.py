import pymysql

def get_district():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='ys1234ys', database='bj_air')
    cursor = conn.cursor()
    cursor.execute('select id, station_name from weather_station')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values

def insert_district(data):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='ys1234ys', database='bj_air')
    cursor = conn.cursor()
    cursor.executemany('insert into district (district_id, district_name) VALUES (%s, %s)', data)
    conn.commit()
    cursor.close()
    conn.close()

insert_district(get_district())