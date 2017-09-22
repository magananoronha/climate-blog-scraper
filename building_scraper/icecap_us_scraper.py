#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:32:26 2017

@author: magananoronha

Scraper for icecap.us  It appears to be custom janky html, but is one of the most 
popular blogs.
"""

from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import uuid


def process(url):
    content = requests.get(url).content
    download_time = datetime.datetime.now()
    post_uuid = str(uuid.uuid4())
    s3.Bucket('climateblogs').put_object(Key=post_uuid, Body=content)
    table.put_item(Item={
            'uuid' : post_uuid,
            'url' : url,
            'homepage' : homepage,
            'download_time' : download_time.strftime("%Y-%m-%d %X")})

if __name__ == '__main__':
    homepage = 'http://icecap.us/index.php/go/joes-blog'
    url_num = 15
    increment = 15
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_metadata')
    s3 = boto3.resource('s3')

    process(homepage)
    
    for i in range(0,89):
        sleep_time = random.randint(60,120)
        print('Sleep Time: {} seconds'.format(sleep_time))
        sleep(sleep_time)
        url = '{}/P{}/'.format(homepage, url_num)
        print(url)
        process(url)
        url_num += increment
        

