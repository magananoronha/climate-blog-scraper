#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:22:53 2017

@author: magananoronha

Copy of scraper that goes from most recent and works backwards.  This one 
starts with first post and moves forwards.  Using for more prolific bloggers.
"""

from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import uuid


def download_page(url):
    download_time = datetime.datetime.now()
    if any(site in url for site in block_list):
        content = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content
    else:
        content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    a_prev = soup.find('a', {'rel':'next'})
    link_prev = soup.find('link', {'rel':'next'})
    a_pager_older = soup.find('a', {'class':'blog-pager-newer-link'})
    if a_prev is not None:
        new_url = a_prev['href']
    elif link_prev is not None:
        new_url = link_prev['href']
    elif a_pager_older is not None:
        new_url = a_pager_older['href']
    else:
        new_url = None
    return download_time, content, new_url


if __name__ == '__main__':
    start_urls = pd.read_csv('second_bot.csv')
    start_urls = start_urls.where((pd.notnull(start_urls)), None)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_metadata')
    s3 = boto3.resource('s3')

    block_list = ['http://www.climatedepot.com/',
                  'http://www.cfact.org/',
                  'http://www.drroyspencer.com/']

    for i in range(0,300):
        sleep_time = random.randint(45,90)
        print('Sleep Time: {} seconds'.format(sleep_time))
        sleep(sleep_time)
        print('Starting Cycle #{}, {} blogs'.format(i, start_urls.count(axis=0)['first_post']))
        for index in range(0,len(start_urls)):
            url = start_urls.loc[index,'first_post']
            print(index, url)
            if (url is not None):
                download_time, content, new_url = download_page(url)
                start_urls.loc[index, 'first_post'] = new_url
                start_urls.to_csv('second_bot.csv',index=False)
                post_uuid = str(uuid.uuid4())
                s3.Bucket('climateblogs').put_object(Key=post_uuid, Body=content)
                table.put_item(Item={
                        'uuid' : post_uuid,
                        'url' : url,
                        'homepage' : start_urls.loc[index,'homepage'],
                        'download_time' : download_time.strftime("%Y-%m-%d %X")})
