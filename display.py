import plotext as plo
import pandas as pd
import time


def get_current_ip_details():
    data = pd.read_csv('data/ip_data.csv')
    data = data.tail(1).reset_index().drop(columns = ['index'])
    return data


def display_graph(points = 120):
    plo.theme('dark')
    plo.title('Ping Data')
    plo.xaxes(False, False)
    plo.yaxes(False, False)
    while True:
        for i in range(5):
            try:
                ping_data = pd.read_csv('data/ping_data.csv').tail(points)
                ip_data = get_current_ip_details()
                break
            except:
                time.sleep(1)
        ping_data = list(ping_data['ping_time'])
        plo.plot(ping_data, marker = 'braille')
        plo.ylabel("City: %s   Region: %s   Country: %s   Current IP: %s" \
            % (ip_data['city'][0], ip_data['region'][0], ip_data['country'][0], ip_data['ip_address'][0]), 'upper')
        #plo.ylabel('Test 3')
        plo.clear_terminal()
        plo.show()
        plo.clear_data()
        time.sleep(1)


display_graph()