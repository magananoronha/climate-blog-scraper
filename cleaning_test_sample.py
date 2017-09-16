#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:53:10 2017

@author: magananoronha

"""

from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import uuid
from collections import defaultdict

if __name__ == '__main__':
    sites = defaultdict(list)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_metadata')

    for i in range(0,2000):
        sleep(10)
        print('Starting Cycle #{}, {} blogs'.format(i, start_urls.count(axis=0)['recent_post']))
        for index in range(0,len(start_urls)):
            url = start_urls.loc[index,'recent_post']
            print(index, url)
            if (url is not None):
                download_time, content, new_url = download_page(url)
                start_urls.loc[index, 'recent_post'] = new_url
                start_urls.to_csv('mix_links.csv',index=False)
                post_uuid = str(uuid.uuid4())
                s3.Bucket('climateblogs').put_object(Key=post_uuid, Body=content)
                table.put_item(Item={
                        'uuid' : post_uuid,
                        'url' : url,
                        'homepage' : start_urls.loc[index,'homepage'],
                        'download_time' : download_time.strftime("%Y-%m-%d %X")})
