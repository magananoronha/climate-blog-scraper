#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:19:17 2017

@author: magananoronha
"""

import pandas as pd
import datetime
import re
from dateutil.parser import parse
from collections import Counter
from difflib import SequenceMatcher


df = pd.read_pickle('../data/postgres_db.pkl')

names = pd.read_pickle('../data/names.pkl')

df.loc[211086,'blog_url'] = 'http://climateaudit.org/'

weird_dates = df[(df.pub_time < pd.Timestamp.min) | (df.pub_time > datetime.datetime.now())]
df.loc[weird_dates.index,'pub_time'] = None

def url_regex(i, df):
    date = re.findall('/(\d{4}/\d{2}/\d{2})', df.loc[i]['url'])
    if date:
        df.loc[i,'pub_time'] = parse(date[0])

null_dates = df[df.pub_time.isnull()]
for i, row in null_dates.iterrows():
    url_regex(i, df)

crazy_dates = df[df.pub_time < datetime.datetime(1990, 1, 1)]
df.loc[crazy_dates.index,'pub_time'] = None

df = df[(df.pub_time).notnull()]

names_list = []
for i in range(len(names)):
    for name in names.iloc[i]['names']:
        names_list.append({'name' : name, 'url' : df.iloc[i]['url']})
        

names_df = pd.DataFrame(names_list)

unique_names = list(set(names_df.name))

counter_names = Counter(names_df.name)

counter_df = pd.DataFrame.from_dict(counter_names, orient='index').reset_index()
counter_df.rename(columns={'index': 'name',0:'count'}, inplace=True)
counter_df.sort_values(by='count',inplace=True, ascending=False)

real_names = []
for name, count in counter_names.most_common():
    if len(name) > 3 and count > 20:
        real_names.append({'name':name, 'count':count})
        
real_names_df = pd.DataFrame(real_names)
real_names_df.sort_values(by='count',inplace=True, ascending=False)

real_names_df.to_pickle('../data/names_to_work.pkl')