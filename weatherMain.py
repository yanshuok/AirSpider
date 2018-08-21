from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import threading
import traceback
from utils import emailUtil
from weather import weatherDAO



def connect(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap['phantomjs.page.customHeaders.Accept'] = (
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    dcap["phantomjs.page.settings.userAgent"] = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    driver = webdriver.PhantomJS(executable_path='/root/PythonProject/phantomjs/bin/phantomjs', desired_capabilities=dcap)

    driver.get(url)
    return driver


def process24h(rawData24h, stationId):
    weatherList = list()
    date = rawData24h['od']['od0'][0:10]
    for index, rawData1h in enumerate(rawData24h['od']['od2']):
        onehour = list()
        onehour.append(stationId)
        onehour.append(date)
        onehour.append(index)
        if rawData1h['od22']=='':
            onehour.append(-99)  # temperature
        else:
            onehour.append(rawData1h['od22'])

        if rawData1h['od27']=='':
            onehour.append(-99)  # humidity
        else:
            onehour.append(rawData1h['od27'])

        if rawData1h['od26']=='':
            onehour.append(-99)
        else:
            onehour.append(rawData1h['od26'])  # rain

        if rawData1h['od25']=='':
            onehour.append(-99)
        else:
            onehour.append(rawData1h['od25'])  # wind_force

        if rawData1h['od23']=='':
            onehour.append(-99)  # wind_direction
        else:
            onehour.append(rawData1h['od23'])
        weatherList.append(onehour)
    return weatherList


def onelink(url):
    while (True):
        print('start', url[0])
        try:
            driver = connect(url[1])
            rawData24h = driver.execute_script('return observe24h_data')
            weather24hList = process24h(rawData24h, url[0])
            weatherDAO.insertWeahter24h(weather24hList)
            driver.close()
            break
        except Exception:
            driver.close()
            continue
    print('finish', url[0])


def executeWeatherSpider():
    print('start collecting weater data')
    try:
        urls = weatherDAO.getUrls()
    except Exception:
        msg = traceback.format_exc()
        emailUtil.send(msg)
        print(msg)
    else:
        for url in urls:
            t = threading.Thread(target=onelink(url))
            t.start()
            t.join()


    print('collect weather data complete!')
