from urllib.request import urlopen
from bs4 import BeautifulSoup
from mysql import connector

def insert_weather_station(stationList):
    conn = connector.connect(user='root', password='ys1234ys', database='bj_air')
    cursor = conn.cursor()
    sql ='insert into weather_station (id, station_name, href) VALUES (%s, %s, %s)'
    cursor.executemany(sql, stationList)
    print(cursor.rowcount)
    conn.commit()
    cursor.close()
    conn.close()


html = urlopen('http://bj.weather.com.cn/')
bs = BeautifulSoup(html, 'lxml')
links =bs.find('div', class_='navbox').find('span').findAll('a')
stationList = list()
for link in links[0:15]:
    station = list()
    href = link.attrs['href']
    station_id = href.split('/')[-1][0:9]
    station_name = link.get_text()
    station.append(station_id)
    station.append(station_name)
    station.append(href)
    stationList.append(station)
insert_weather_station(stationList)


