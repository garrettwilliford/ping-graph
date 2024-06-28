import requests
import time
import datetime
import pandas as pd
import json
import os


def get_ip():
    return requests.get('https://api.ipify.org').content.decode('utf8')


def get_ip_details(ip_address):
    response = json.loads(requests.get('http://ipinfo.io/json').content)
    data = pd.DataFrame({
        'timezone'       : [time.tzname[0]],
        'active_date'    : [str(datetime.datetime.now().replace(microsecond = 0))],
        'ip_address'     : [ip_address],
        'country'        : [response['country']],
        'region'         : [response['region']],
        'city'           : [response['city']]
    })
    return data


def ip_logger():
    no_current_ip = False
    while True:
        current_ip = get_ip()
        if not os.path.isfile('data/current_ip.txt'):
            open('data/current_ip.txt', 'w').write(current_ip)
            previous_ip = current_ip
            no_current_ip = True
        else:
            previous_ip = open('data/current_ip.txt', 'r').read()
        if previous_ip != current_ip or no_current_ip:
            open('data/current_ip.txt', 'w').write(current_ip)
            data = get_ip_details(current_ip)
            if not os.path.isfile('data/ip_data.csv'):
                data.to_csv('data/ip_data.csv', mode = 'w', header = True, index = False)
            else:
                data.to_csv('data/ip_data.csv', mode = 'a', header = False, index = False)
        if no_current_ip:
            no_current_ip = False
        time.sleep(1)


ip_logger()