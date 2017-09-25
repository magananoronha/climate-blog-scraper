#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:17:55 2017

@author: magananoronha
"""

import boto3
import psycopg2
from customclasses import extractors
from time import gmtime, strftime
    
def insert_items(items):
    for i in range(len(items)):
        post = items[i]
        cursor.execute("""SELECT exists(select 1 from blogs WHERE url = %s);""",(post['homepage'],))
        blog_exists = cursor.fetchall()[0][0]
        cursor.execute("""SELECT exists(select 1 from posts WHERE uuid = %s);""",(post['uuid'],))
        post_in_db = cursor.fetchall()[0][0]
        if blog_exists and not post_in_db:
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
    
    #cursor.execute('DROP TABLE blogs CASCADE;')
    
    #cursor.execute('DROP TABLE posts CASCADE;')
#    
#    with open('../building_postgres/db_schema.sql') as f:
#        sql = f.read()
#        
#    cursor.execute(sql)
#    print('made tables')
#    blog_table = pd.read_csv('classnames.csv')
#    
#    for i in range(len(blog_table)):
#        cursor.execute( """INSERT INTO blogs (url, cleaning_class) 
#                            VALUES (%s, %s);""",(blog_table.iloc[i]['homepage'],
#                                                 blog_table.iloc[i]['className']))
#    print('populated blog table')
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
