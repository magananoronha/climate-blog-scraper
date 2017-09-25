#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:17:55 2017

@author: magananoronha
"""

import boto3
import botocore
import psycopg2
from customclasses import extractors
from time import gmtime, strftime

def check_s3_key(post):
    exists = False
    try:
        s3.head_object(Bucket='climateblogs', Key=post['uuid'])
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            exists = False
        else:
            raise
    else:
        exists = True
    return exists
    
def insert_items(items):
    for i in range(len(items)):
        post = items[i]
        cursor.execute("""SELECT exists(select 1 from blogs WHERE url = %s);""",(post['homepage'],))
        blog_exists = cursor.fetchall()[0][0]
        cursor.execute("""SELECT exists(select 1 from posts WHERE uuid = %s);""",(post['uuid'],))
        post_in_db = cursor.fetchall()[0][0]
        file_exists = check_s3_key(post)
        if blog_exists and file_exists and not post_in_db:
            post['content'] = s3.get_object(Bucket='climateblogs', Key=post['uuid'])['Body'].read()
            cursor.execute("""SELECT cleaning_class FROM blogs WHERE url = %s;""",(post['homepage'],))
            method = cursor.fetchall()[0][0]
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
    
    print('connected to dynamo')

    s3 = boto3.client('s3')

    print('connected to s3')
    
    with open('postgres_password.txt') as f:
        password = f.read().strip()
    
    conn = psycopg2.connect(database='climateblogsdb', user='magananoronha', password=password,
        host='climateblogdb.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
        connect_timeout=10)
    
    conn.autocommit = True
    
    print('connected to postgres')
    
    password = None
    
    cursor = conn.cursor()
    
    response = table.scan()
    insert_items(response['Items'])
    
    while True:
        print(len(response['Items']))
        if response.get('LastEvaluatedKey'):
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            insert_items(response['Items'])
            print(response['LastEvaluatedKey'])
            print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        else:
            break
    
    conn.commit()
    conn.close()
