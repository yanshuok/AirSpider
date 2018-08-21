from airquality import AirQualityMain
from weather import weatherMain
import threading
from datetime import datetime


def main():
    print('collectingstart:',datetime.now())
    t1 = threading.Thread(target=AirQualityMain.executeAirSpider)
    t2 = threading.Thread(target=weatherMain.executeWeatherSpider)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
