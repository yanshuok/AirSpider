from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import threading
import traceback
from datetime import datetime
from utils import emailUtil, CONST
from weather.weatherDAO import getUrls, insertWeahter24h
valid_keys = ['od22', 'od27', 'od26', 'od25', 'od23']
keys = ['temperature', 'humidity', 'rain', 'wind_force', 'wind_direction']


def connect(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap['phantomjs.page.customHeaders.Accept'] = (
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    dcap["phantomjs.page.settings.userAgent"] = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    driver = webdriver.PhantomJS(executable_path=CONST.browser_path, desired_capabilities=dcap)
    driver.get(url)
    return driver


def process24h(rawData24h, stationId):
    weatherList = list()
    date = rawData24h['od']['od0'][0:10]
    for index, rawData1h in enumerate(rawData24h['od']['od2']):
        onehour = dict()
        onehour['station_id'] = stationId
        onehour['date'] = datetime(year=int(date[:4]), month=int(date[4:6]), day=int(date[6:8]), hour=int(date[8:10]))
        onehour['dur'] = index
        for key, valid_key in zip(keys, valid_keys):
            if rawData1h[valid_key] != '' and rawData1h[valid_key] != 'null':
                onehour[key] = rawData1h[valid_key]

        weatherList.append(onehour)
    return weatherList


def onelink(url):
    print('start', url.id)
    driver = connect(url.href)
    rawData24h = driver.execute_script('return observe24h_data')
    weather24hList = process24h(rawData24h, url.id)
    insertWeahter24h(weather24hList)
    driver.close()
    print('finish', url.id)


def execute_weather_spider():
    print('start collecting weater data')
    try:
        urls = getUrls()
        for url in urls:
            t = threading.Thread(target=onelink(url))
            t.start()
            t.join()
    except Exception as e:
        msg = traceback.format_exc()
        emailUtil.send('++new++'+msg)
        print(msg)
    print('collect weather data complete!')
