#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:12:56 2017
@author: magananoronha
First complete webscraper after the Watts Up With That test.  Scraping mostly
Wordpress blogs, but works on anything that defines that previous post url 
using the <a rel=prev> or <link rel=prev> tags.  Puts post content into S3 bucket
and post metadata into a DynamoDB table.  
"""

from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import uuid
import wget
import urllib
import os

def download_page(url):
    download_time = datetime.datetime.now()
    if any(site in url for site in block_list):
        content = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content
    elif url == 'http://www.coyoteblog.com/':
	filename = wget.download(url)
	content = urllib.urlopen(filename).read()
	os.remove(filename)	
    else:
        content = requests.get(url).content
    soup = BeautifulSoup(content)
    a_prev = soup.find('a', {'rel':'prev'})
    link_prev = soup.find('link', {'rel':'prev'})
    a_pager_older = soup.find('a', {'class':'blog-pager-older-link'})
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
    start_urls = pd.read_csv('mix_links.csv')
    start_urls = start_urls.where((pd.notnull(start_urls)), None)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('climateblog_metadata')
    s3 = boto3.resource('s3')

    block_list = ['http://www.climatedepot.com/',
                  'http://www.cfact.org/',
                  'http://www.drroyspencer.com/']

    for i in range(0,200000):
        sleep_time = random.randint(10,15)
        print('Sleep Time: {} seconds'.format(sleep_time))
        sleep(sleep_time)
        print('Starting Cycle #{}, {} blogs'.format(i, start_urls.count(axis=0)['recent_post']))
        for index in range(0,len(start_urls)):
            url = start_urls.loc[index,'recent_post']
            print(index, url)
            if (url is not None):
                check = table.get_item(Key={'url':url})
                if 'Item' in check.keys():
                    start_urls.loc[index, 'recent_post'] = None
                else:
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
