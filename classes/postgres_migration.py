#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:17:55 2017

@author: magananoronha
"""

from time import sleep
import pandas as pd
import boto3
import psycopg2
from customclasses import extractors


    
def insert_items(items):
    for i in range(len(items)):
        post = items[i]
        blog = blog_table[blog_table.homepage == post['homepage']]
        if len(blog) != 0:
            post['content'] = s3.get_object(Bucket='climateblogs', Key=post['uuid'])['Body'].read()
            method = blog.iloc[0]['className']
            method_to_call = getattr(extractors, method)
            result = method_to_call(post['content'])        
            cursor.execute( """INSERT INTO posts (url, uuid, download_date, blog_url, title, author, pub_date, body) 
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",(post['url'],
                                                   post['uuid'],
                                                   post['download_time'],
                                                   post['homepage'],
                                                   result.title,
                                                   result.author,
                                                   result.pub_time,
                                                   result.body))
          
if __name__ == '__main__':
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('climateblog_metadata')
    
    s3 = boto3.client('s3')
    
    with open('postgres_password.txt') as f:
        password = f.read().strip()
    
    conn = psycopg2.connect(database='climateblogsdb', user='magananoronha', password=password,
        host='climateblogdb.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
        connect_timeout=10)
    
    
    password = None
    
    cursor = conn.cursor()
    
    #cursor.execute('DROP TABLE blogs CASCADE;')
    
    #cursor.execute('DROP TABLE posts CASCADE;')
#    
    with open('../building_postgres/db_schema.sql') as f:
        sql = f.read()
        
    cursor.execute(sql)
    
    blog_table = pd.read_csv('classnames.csv')
    
    for i in range(len(blog_table)):
        cursor.execute( """INSERT INTO blogs (url, cleaning_class) 
                            VALUES (%s, %s);""",(blog_table.iloc[i]['homepage'],
                                                 blog_table.iloc[i]['className']))
    
    response = table.scan()
    insert_items(response['Items'])
    
    while True:
        print(len(response['Items']))
        if response.get('LastEvaluatedKey'):
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            insert_items(response['Items'])
        else:
            break
    
    conn.commit()
    conn.close()