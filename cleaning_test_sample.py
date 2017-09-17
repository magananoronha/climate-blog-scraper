#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:53:10 2017

@author: magananoronha

"""

from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import datetime
import random
import boto3


def make_soup(content):
    soup = BeautifulSoup(content,'lxml')
    return soup


def get_title(soup):
    title_1 = soup.find_all(class_='entry-title') #watts
    title_2 = soup.find_all(class_='post-title') #motls


    title_tag = soup.find('div', {'class':'post-header'}) 
        

def get_author(soup):
    author_1 = soup.find('a', {'class':'author'}) #watts
    author_2 = soup.find('span', {'class':'post-author'}) #motls
    author_3 = soup.find('span', {'class':'author-name'}) 

    
    
    author_tag = soup.find('a', {'rel':'author'})

    
def get_pubtime(soup):
    title_tag = soup.find('meta', {'property':'article:published_time'}) #get the content
    title_tag = soup.find_all(class_='date-header') #motls
    author_tag = soup.find('a', {'class':'timestamp-link'}) #motls
    author_tag = soup.find('abbr', {'class':'published'}) #motls



def get_body(soup):
    author_tag = soup.find('div', {'class':'entry-content'}) #watts
    author_tag = soup.find('div', {'class':'post-body'}) #motls

    

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('post_metadata')

    s3 = boto3.client('s3')
    
    response = table.scan()
    
    for item in response['Items']:
        sleep(5)
        post_uuid = item['uuid']
        download_time = item['download_time']
        url = item['url']
        homepage = item['homepage']
        
        content = s3.get_object(Bucket='climateblogs', Key=post_uuid)['Body'].read()
        soup = make_soup(content)
        
        
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
