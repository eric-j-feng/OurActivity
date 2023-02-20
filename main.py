"""
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




def print_hi(name):
   # Use a breakpoint in the code line below to debug your script.
   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.pyplot import figure
from matplotlib.dates import DateFormatter
import requests


def grab_oura_json(file_path):
    with open(file_path) as sleep_file:
        data = json.load(sleep_file)
        return data


if __name__ == '__main__':
    # API request
    url = 'https://api.ouraring.com/v2/usercollection/daily_sleep'
    params = {
        'start_date': '2022-11-01',
        'end_date': '2022-12-01'
    }
    headers = {
        'Authorization': 'Bearer 5CR4QYQOQ5C2PB2YKYUC3ZOWPCV2WYTO'
    }
    response = requests.request('GET', url, headers=headers, params=params)

    # Convert to response to JSON, write to file
    file_path = 'data/sleep.json'
    data = None
    with open(file_path, 'w') as outfile:
        json.dump(response.json(), outfile)

    with open(file_path) as f:
        data = json.loads(f.read())

    byDate = data["data"]
    table1 = pd.DataFrame.from_dict(byDate)
    print(table1["contributors"][0]['deep_sleep'])
    table1.info()

# df = pd.DataFrame.from_dict()
