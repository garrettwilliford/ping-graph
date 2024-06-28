import os
import datetime
import time
import pandas as pd


def ping(ping_ip = '8.8.8.8'):
    os.system(f'ping -c 1 {ping_ip} > data/static_ping.txt')


def loop_overwrite():
    data = pd.read_csv('data/ping_data.csv')
    data = data.tail(60).reset_index().drop(columns = ['index'])
    data.to_csv('data/ping_data.csv', mode = 'w', header = True, index = False)


def ping_logger(overwrite = True, loop_overwrite_count = 200):
    if overwrite:
        try:
            _output = os.system('rm data/ping_data.csv')
        except:
            pass
    while True:
        for i in range(loop_overwrite_count):
            try:
                ping()
                time.sleep(1)
                with open('data/static_ping.txt', 'r') as file:
                    data = file.readlines()
                data = pd.DataFrame({
                    'current_date' : [str(datetime.datetime.now().replace(microsecond = 0))], 
                    'ping_time'    : [float(data[1][data[1].index('time=') + 5:data[1].index(' ms')])]
                })
                if os.path.isfile('data/ping_data.csv'):
                    data.to_csv('data/ping_data.csv', mode = 'a', index = False, header = False)
                else:
                    data.to_csv('data/ping_data.csv', mode = 'w', index = False, header = True)
            except:
                time.sleep(1)
        if overwrite:
            loop_overwrite()


ping_logger()        