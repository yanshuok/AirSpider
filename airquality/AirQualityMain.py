import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from airquality.airDAO import insertAirQaulity, getStationIds
from utils import emailUtil, CONST


def connect():
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap['phantomjs.page.customHeaders.Accept']=('text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    driver = webdriver.PhantomJS(executable_path=CONST.browser_path,desired_capabilities=dcap)

    url = 'http://zx.bjmemc.com.cn/getAqiList.shtml'
    timestamp = str(datetime.now().timestamp())
    url = url+'?timestamp='+ timestamp[0:10]+timestamp[11:13]
    driver.get(url)
    return driver


valid_keys = ['co_02','co', 'co_01', 'no2_02', 'no2', 'no2_01','so2_02','so2','so2_01','o3_02','o3','o3_01','pm2_02', 'pm2','pm2_01','pm10_02','pm10', 'pm10_01', 'first', 'grade', 'aqi', 'date_f', 'id']
keys = ['co_0', 'co_iaqi', 'co', 'no2_0', 'no2_iaqi', 'no2', 'so2_0', 'so2_iaqi', 'so2', 'o3_0', 'o3_iaqi', 'o3', 'pm25_0', 'pm25_iaqi', 'pm25', 'pm10_0', 'pm10_iaqi', 'pm10','first', 'grade', 'aqi', 'date', 'station_id']
def process_single(x):
    air = {}
    for key, valid_key in zip(keys, valid_keys):
        try:
            if valid_key == 'date_f':
                air[key] = datetime.fromtimestamp(int(x[valid_key]))
            else:
                air[key] = x[valid_key]
        except KeyError as e:
            print(valid_key, e)
    return air


def process_rawData(airRawData):
    airList = list()
    stationIds = getStationIds()
    for x in airRawData:
        if x['id'] in stationIds:
            air = process_single(x)
            airList.append(air)
    return airList


def searchStationId(id, stationIds):
    for x in stationIds:
        if id==x[0]:
            return True
    return False

def execute_air_spider():
    print('start collecting airquality data')
    try:
        driver =connect()
        airRawData = driver.execute_script('return wfelkfbnx')
        airList = process_rawData(airRawData)
        insertAirQaulity(airList)
        driver.close()
    except Exception:
        msg = traceback.format_exc()
        emailUtil.send('++new++'+msg)
        print(msg)
        print(airRawData)
    print('collect airquality data complete')
