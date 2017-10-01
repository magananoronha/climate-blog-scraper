#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:18:08 2017

@author: magananoronha

Finished moving data into PostgresDB.  Did a select * on the post table
and saved it as a pickle file locally.  Doing some first pass EDA on the data.
"""

import pandas as pd
import psycopg2


with open('postgres_password.txt') as f:
    password = f.read().strip()

conn = psycopg2.connect(database='gwblog', user='magananoronha', password=password,
    host='gwblog.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
    connect_timeout=10)


conn.autocommit = True

print('connected to postgres')

password = None

cursor = conn.cursor()

cursor.execute('SELECT * FROM posts;')

tmp = cursor.fetchall()

data = pd.read_pickle('../data/postgres_sample.pkl')
df = pd.DataFrame(tmp, columns=['url','uuid','download_time','blog_url','title','author','pub_time','body','prev_post','next_post'])
df['word_count'] = [len(x.split()) if x is not None else 0 for x in df.body]

df.to_pickle('postgres_db.pkl')