import csv
import json
import pandas as pd
import numpy as np
from datetime import date, timedelta
import urllib
import codecs

def openaq_data(start_date, end_date, param):
    base_url = 'https://openaq-data.s3.amazonaws.com/'
    current_date = start_date
    date_list = []
    while current_date < end_date:
        current_date_string = current_date.strftime('%Y-%m-%d')
        try:
            data = urllib.request.urlopen(base_url + current_date_string + '.csv')
            contents = csv.reader(codecs.iterdecode(data, 'utf-8'))
            raw_observations = list(contents)

            df = pd.DataFrame(raw_observations)
            df.columns = ['location','city','country','utc','local','parameter','value',
                          'unit','latitude','longitude','attribution']
            df = df[df['parameter'] == param]

            date_list.append(df)
            print('Done with ' + current_date_string)
            current_date = current_date + timedelta(days=1)
        except urllib.error.HTTPError as e:
            print(current_date_string + '.csv does not exist')
            current_date = current_date + timedelta(days=1)
            continue

    open_data = pd.concat(date_list)

    return open_data
