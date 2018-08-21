import datetime
import traceback

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from airquality import airDAO
from utils import emailUtil


def connect():
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap['phantomjs.page.customHeaders.Accept']=('text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    driver = webdriver.PhantomJS(executable_path='/root/PythonProject/phantomjs/bin/phantomjs',desired_capabilities=dcap)

    url = 'http://zx.bjmemc.com.cn/getAqiList.shtml'
    timestamp = str(datetime.datetime.now().timestamp())
    url = url+'?timestamp='+ timestamp[0:10]+timestamp[11:13]
    driver.get(url)
    return driver


def process_single(x):
    air = list()
    air.append(x['co_02'])
    air.append(x['co'])
    air.append(x['co_01'])
    air.append(x['no2_02'])
    air.append(x['no2'])
    air.append(x['no2_01'])
    air.append(x['so2_02'])
    air.append(x['so2'])
    air.append(x['so2_01'])
    air.append(x['o3_02'])
    air.append(x['o3'])
    air.append(x['o3_01'])
    air.append(x['pm2_02'])
    air.append(x['pm2'])
    air.append(x['pm2_01'])
    air.append(x['pm10_02'])
    air.append(x['pm10'])
    air.append(x['pm10_01'])
    air.append(x['first'])
    air.append(x['grade'])
    air.append(x['aqi'])
    air.append(x['date_f'])
    air.append(x['id'])
    return air


def process_rawData(airRawData):
    airList = list()
    stationIds = airDAO.getStationIds()
    for x in airRawData:
        if searchStationId(x['id'], stationIds):
            air = process_single(x)
            airList.append(air)
    return airList


def searchStationId(id, stationIds):
    for x in stationIds:
        if id==x[0]:
            return True
    return False

def executeAirSpider():
    print('start collecting airquality data')
    try:
        driver =connect()
        airRawData = driver.execute_script('return wfelkfbnx')
        airList = process_rawData(airRawData)
        airDAO.insertAirQaulity(airList)
        driver.close()
    except Exception:
        msg = traceback.format_exc()
        emailUtil.send(msg)
        print(msg)
        print(airRawData)
    print('collect airquality data complete')
