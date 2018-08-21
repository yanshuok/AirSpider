from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import threading
import traceback
from datetime import datetime
from utils import emailUtil
from weather.weatherDAO import getUrls, insertWeahter24h
valid_keys = ['od22', 'od27', 'od26', 'od25', 'od23']
keys = ['temperature', 'humidity', 'rain', 'wind_force', 'wind_direction']


def connect(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap['phantomjs.page.customHeaders.Accept'] = (
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    dcap["phantomjs.page.settings.userAgent"] = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    #driver = webdriver.PhantomJS(executable_path='/root/PythonProject/phantomjs/bin/phantomjs', desired_capabilities=dcap)
    driver = webdriver.PhantomJS(executable_path='D:/Study/DevelopmentTools/phantomjs-2.1.1-windows/bin/phantomjs',desired_capabilities=dcap)
    driver.get()
    return driver

driver = connect('http://www.baidushabi.com/', )
d