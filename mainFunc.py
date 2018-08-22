from airquality import AirQualityMain
from weather import weatherMain
from visibility import visibilityMain
import threading
from datetime import datetime


def main():
    print('collectingstart:',datetime.now())
    t1 = threading.Thread(target=AirQualityMain.execute_air_spider())
    t2 = threading.Thread(target=weatherMain.execute_weather_spider())
    t3 = threading.Thread(target=visibilityMain.execute_visibility_spider())
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()
