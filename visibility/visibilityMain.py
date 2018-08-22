import requests, traceback
from datetime import date, datetime
from utils import emailUtil
from visibility.visibilityDAO import insert_visibility, get_districts

def get_final_data():
    final_data = []
    cities = get_districts()
    for x in cities:
        i = x.id
        city = x.station_name
        params = {'key': '56bafcc8438742898b65aa31b513479b', 'location': city+',北京'}
        res = requests.get('https://free-api.heweather.com/s6/weather/now?parameters', params=params)
        data = res.json()['HeWeather6'][0]
        now = data['now']
        update = data['update']
        local_time = update['loc']
        final_data.append({'feel_temperature':now['fl'],
                           'temperature': now['tmp'],
                          'weather': now['cond_code'],
                          'wind_direction': now['wind_deg'],
                          'wind_power': now['wind_spd'],
                          'humidity': now['hum'],
                          'precipitation': now['pcpn'],
                          'press': now['pres'],
                          'visibility': now['vis'],
                          'cloud': now['cloud'],
                          'date': datetime.strptime(local_time, '%Y-%m-%d %H:%M'),
                          'district_id': i})
    return final_data

def execute_visibility_spider():
    print('Visibility collecting start:', datetime.now())
    try:
        data = get_final_data()
        insert_visibility(data)
    except Exception:
        msg = traceback.format_exc()
        emailUtil.send(msg)
        print(msg)
    print('Visibility collecting complete:', datetime.now())