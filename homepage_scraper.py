#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:28:23 2017

@author: magananoronha

Manually generated a list of 119 blogs that argue views opposing scientific consensus of anthropogenic global warming.  Preparing data to be inserted into a nosql db, most likely DynamoDB.

Getting homepage content and extracting platform type
"""

import requests
import pickle
import pandas as pd
from time import sleep

if __name__ == '__main__':
    df = pd.read_csv('blogs_subset.csv')
    df['page_content'] = ''
    for index, row in df.iterrows():
        sleep(10)
        row.page_content = requests.get(row.recent_post).content
    df.to_pickle('first_page.pkl')
