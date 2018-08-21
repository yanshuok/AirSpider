import mysql.connector

a =[{"StationNumber":"1","StationName":"永定门"},{"StationNumber":"2","StationName":"京南"},{"StationNumber":"3","StationName":"香山"},{"StationNumber":"5","StationName":"丰台花园"},{"StationNumber":"6","StationName":"顺义"},{"StationNumber":"7","StationName":"延庆"},{"StationNumber":"8","StationName":"平谷"},{"StationNumber":"9","StationName":"房山"},{"StationNumber":"10","StationName":"亦庄"},{"StationNumber":"11","StationName":"云岗"},{"StationNumber":"12","StationName":"京东北"},{"StationNumber":"13","StationName":"怀柔"},{"StationNumber":"14","StationName":"京西北"},{"StationNumber":"15","StationName":"万寿西宫"},{"StationNumber":"17","StationName":"昌平"},{"StationNumber":"18","StationName":"门头沟"},{"StationNumber":"19","StationName":"通州"},{"StationNumber":"20","StationName":"大兴"},{"StationNumber":"21","StationName":"定陵"},{"StationNumber":"23","StationName":"前门"},{"StationNumber":"24","StationName":"东四"},{"StationNumber":"25","StationName":"天坛"},{"StationNumber":"26","StationName":"奥体中心"},{"StationNumber":"27","StationName":"农展馆"},{"StationNumber":"28","StationName":"密云"},{"StationNumber":"29","StationName":"古城"},{"StationNumber":"32","StationName":"官园"},{"StationNumber":"34","StationName":"南三环"},{"StationNumber":"37","StationName":"北部新区"},{"StationNumber":"38","StationName":"万柳"},{"StationNumber":"40","StationName":"京东南"},{"StationNumber":"41","StationName":"京西南"},{"StationNumber":"43","StationName":"京东"},{"StationNumber":"46","StationName":"东四环"},{"StationNumber":"47","StationName":"西直门"}]
b =[{"list":[{"heng":"116.394","shu":"39.876"}],"zname":"1"},{"list":[{"heng":"116.30","shu":"39.52"}],"zname":"2"},{"list":[{"heng":"116.207","shu":"40.002"}],"zname":"3"},{"list":[{"heng":"116.279","shu":"39.863"}],"zname":"5"},{"list":[{"heng":"116.655","shu":"40.127"}],"zname":"6"},{"list":[{"heng":"115.972","shu":"40.453"}],"zname":"7"},{"list":[{"heng":"117.1","shu":"40.143"}],"zname":"8"},{"list":[{"heng":"116.136","shu":"39.742"}],"zname":"9"},{"list":[{"heng":"116.506","shu":"39.795"}],"zname":"10"},{"list":[{"heng":"116.146","shu":"39.824"}],"zname":"11"},{"list":[{"heng":"116.911","shu":"40.499"}],"zname":"12"},{"list":[{"heng":"116.628","shu":"40.328"}],"zname":"13"},{"list":[{"heng":"115.988","shu":"40.365"}],"zname":"14"},{"list":[{"heng":"116.352","shu":"39.878"}],"zname":"15"},{"list":[{"heng":"116.234","shu":"40.217"}],"zname":"17"},{"list":[{"heng":"116.106","shu":"39.937"}],"zname":"18"},{"list":[{"heng":"116.663","shu":"39.886"}],"zname":"19"},{"list":[{"heng":"116.404","shu":"39.718"}],"zname":"20"},{"list":[{"heng":"116.22","shu":"40.292"}],"zname":"21"},{"list":[{"heng":"116.395","shu":"39.899"}],"zname":"23"},{"list":[{"heng":"116.417","shu":"39.929"}],"zname":"24"},{"list":[{"heng":"116.407","shu":"39.886"}],"zname":"25"},{"list":[{"heng":"116.397","shu":"39.982"}],"zname":"26"},{"list":[{"heng":"116.461","shu":"39.937"}],"zname":"27"},{"list":[{"heng":"116.832","shu":"40.37"}],"zname":"28"},{"list":[{"heng":"116.184","shu":"39.914"}],"zname":"29"},{"list":[{"heng":"116.339","shu":"39.929"}],"zname":"32"},{"list":[{"heng":"116.368","shu":"39.856"}],"zname":"34"},{"list":[{"heng":"116.174","shu":"40.09"}],"zname":"37"},{"list":[{"heng":"116.287","shu":"39.987"}],"zname":"38"},{"list":[{"heng":"116.783","shu":"39.712"}],"zname":"40"},{"list":[{"heng":"116.00","shu":"39.58"}],"zname":"41"},{"list":[{"heng":"117.12","shu":"40.10"}],"zname":"43"},{"list":[{"heng":"116.483","shu":"39.939"}],"zname":"46"},{"list":[{"heng":"116.349","shu":"39.954"}],"zname":"47"}]
c =[{"StationNumber":"1","StationName":"永定门交通点"},{"StationNumber":"2","StationName":"京南区域点"},{"StationNumber":"3","StationName":"海淀北京植物园"},{"StationNumber":"5","StationName":"丰台花园"},{"StationNumber":"6","StationName":"顺义新城"},{"StationNumber":"7","StationName":"延庆镇"},{"StationNumber":"8","StationName":"平谷镇"},{"StationNumber":"9","StationName":"房山良乡"},{"StationNumber":"10","StationName":"亦庄开发区"},{"StationNumber":"11","StationName":"丰台云岗"},{"StationNumber":"12","StationName":"京东北区域点"},{"StationNumber":"13","StationName":"怀柔镇"},{"StationNumber":"14","StationName":"京西北区域点"},{"StationNumber":"15","StationName":"西城万寿西宫"},{"StationNumber":"17","StationName":"昌平镇"},{"StationNumber":"18","StationName":"门头沟龙泉镇"},{"StationNumber":"19","StationName":"通州新城"},{"StationNumber":"20","StationName":"大兴黄村镇"},{"StationNumber":"21","StationName":"定陵对照点"},{"StationNumber":"23","StationName":"前门交通点"},{"StationNumber":"24","StationName":"东城东四"},{"StationNumber":"25","StationName":"东城天坛"},{"StationNumber":"26","StationName":"朝阳奥体中心"},{"StationNumber":"27","StationName":"朝阳农展馆"},{"StationNumber":"28","StationName":"密云镇"},{"StationNumber":"29","StationName":"石景山古城"},{"StationNumber":"32","StationName":"西城官园"},{"StationNumber":"34","StationName":"南三环交通点"},{"StationNumber":"37","StationName":"海淀北部新区"},{"StationNumber":"38","StationName":"海淀万柳"},{"StationNumber":"40","StationName":"京东南区域点"},{"StationNumber":"41","StationName":"京西南区域点"},{"StationNumber":"43","StationName":"京东区域点"},{"StationNumber":"46","StationName":"东四环交通点"},{"StationNumber":"47","StationName":"西直门交通点"}]
count=0
stationList = list()
for x in b:
    alist = list()
    alist.append(x['zname'])
    for y in a:
        if x['zname']==y['StationNumber']:
            alist.append(y['StationName'])
    alist.append(x['list'][0]['heng'])
    alist.append(x['list'][0]['shu'])
    for z in c:
        if x['zname']==z['StationNumber']:
            alist.append(z['StationName'])
    stationList.append(alist)


conn = mysql.connector.connect(user='root', password='ys1234ys',database='bj_air')
cursor = conn.cursor()
cursor.executemany('insert into airquality_station (id, station_name, longitude, altitude, station_detail) VALUES (%s,%s,%s,%s,%s)', stationList)
conn.commit()
print(cursor.rowcount)

cursor.close()
conn.close()

