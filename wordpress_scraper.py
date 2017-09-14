#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:12:56 2017

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
import numpy as np


def download_page(url):
    download_time = datetime.datetime.now()
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    a_prev = soup.find('a', {'rel':'prev'})
    link_prev = soup.find('link', {'rel':'prev'})
    if a_prev is not None:
        new_url = a_prev['href']
    elif link_prev is not None:
        new_url = link_prev['href']
    else:
        new_url = None
    return download_time, content, new_url


if __name__ == '__main__':
    start_urls = pd.read_csv('blog_links.csv')
    start_urls = start_urls.where((pd.notnull(start_urls)), None)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_metadata')
    s3 = boto3.resource('s3')


    for i in range(0,2000):
        sleep_time = random.randint(60,120)
        print('Sleep Time: {} seconds'.format(sleep_time))
        sleep(sleep_time)
        print('Starting Cycle #{}, {} blogs'.format(i, start_urls.count(axis=0)['recent_post']))
        for index in range(0,len(start_urls)):
            url = start_urls.loc[index,'recent_post']
            print(index, url)
            if (url is not None):
                download_time, content, new_url = download_page(url)
                start_urls.loc[index, 'recent_post'] = new_url
                start_urls.to_csv('blog_links.csv',index=False)
                post_uuid = str(uuid.uuid4())
                s3.Bucket('climateblogs').put_object(Key=post_uuid, Body=content)
                table.put_item(Item={
                        'uuid' : post_uuid,
                        'url' : url,
                        'homepage' : start_urls.loc[index,'homepage'],
                        'download_time' : download_time.strftime("%Y-%m-%d %X")})
