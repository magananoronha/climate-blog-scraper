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

toy_data = pd.read_pickle('../data/feature_extract_toy.pkl')

toy_data = toy_data.groupby('homepage').apply(lambda x :x.iloc[random.choice(range(0,len(x)))])
toy_data.reset_index(drop=True, inplace=True)

blog_table = pd.read_csv('classnames.csv')

conn = psycopg2.connect(database='testdb', user='magananoronha', password=password,
    host='testdb.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
    connect_timeout=10)

conn = psycopg2.connect(dbname='blogtest', user='postgres', host='/tmp')

cursor = conn.cursor()

problem_children = []
for i in range(len(toy_data)):
    post = toy_data.iloc[i]
    blog = blog_table[blog_table.homepage == post.homepage]
    if len(blog) != 0:
        method = blog.iloc[0]['className']
        method_to_call = getattr(extractors, method)
        result = method_to_call(post.content)
        if result.body is None:
            problem_children.append(method)
        
print(problem_children)

#dynamodb = boto3.resource('dynamodb')
#table = dynamodb.Table('climateblog_metadata')
#
#s3 = boto3.client('s3')
#
#response = table.scan(Limit=5000)
#items = response['Items']