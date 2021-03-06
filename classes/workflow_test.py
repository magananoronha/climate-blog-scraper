#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:27:42 2017

@author: magananoronha

The entire contents of scraped blogs is being stored in an S3 bucket, with 
file metadata stored in a DynamoDB table.

Built Python classes for each blog that extracts structured data from 
S3 files.  

Goal if this script is to test scripting the process of getting file from S3,
extracting data with classes, and inserting data into Postgres
"""


from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import psycopg2
from customclasses import extractors

with open('postgres_password.txt') as f:
    password = f.read().strip()

#conn = psycopg2.connect(database='testdb', user='magananoronha', password=password,
#    host='testdb.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
#    connect_timeout=10)

conn = psycopg2.connect(database='testdb', user='postgres')

password = None

cursor = conn.cursor()

with open('../building_postgres/db_schema.sql') as f:
    sql = f.read()
    
cursor.execute(sql)

blog_table = pd.read_csv('classnames.csv')

for i in range(len(blog_table)):
    cursor.execute( """INSERT INTO blogs (url, cleaning_class) 
                        VALUES (%s, %s);""",(blog_table.iloc[i]['homepage'],
                                             blog_table.iloc[i]['className']))


toy_data = pd.read_pickle('../data/feature_extract_toy.pkl')

toy_data = toy_data.groupby('homepage').apply(lambda x :x.iloc[random.choice(range(0,len(x)))])
toy_data.reset_index(drop=True, inplace=True)


for i in range(len(toy_data)):
    post = toy_data.iloc[i]
    blog = blog_table[blog_table.homepage == post.homepage]
    if len(blog) != 0:
        method = blog.iloc[0]['className']
        method_to_call = getattr(extractors, method)
        result = method_to_call(post.content)        
        cursor.execute( """INSERT INTO posts (url, uuid, download_date, blog_url, title, author, pub_date, body) 
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",(post.url,
                                               post.uuid,
                                               post.download_time,
                                               post.homepage,
                                               result.title,
                                               result.author,
                                               result.pub_time,
                                               result.body))

        
