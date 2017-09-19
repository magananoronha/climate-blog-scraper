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


def get_prev(soup):
    a_prev = soup.find('a', {'rel':'prev'})
    link_prev = soup.find('link', {'rel':'prev'})
    a_pager_older = soup.find('a', {'class':'blog-pager-older-link'})
    if a_prev is not None:
        prev_url = a_prev['href']
    elif link_prev is not None:
        prev_url = link_prev['href']
    elif a_pager_older is not None:
        prev_url = a_pager_older['href']
    else:
        prev_url = None
    return prev_url


def get_next(soup):
    a_next = soup.find('a', {'rel':'next'})
    link_next = soup.find('link', {'rel':'next'})
    a_pager_older = soup.find('a', {'class':'blog-pager-newer-link'})
    if a_next is not None:
        next_url = a_next['href']
    elif link_next is not None:
        next_url = link_prev['href']
    elif a_pager_older is not None:
        next_url = a_pager_older['href']
    else:
        next_url = None
    return next_url


def scan_for_title_tags(soup):
    entry_title = soup.find(class_='entry-title')
    if entry_title is not None:
        return entry_title.text, 'entry_title'
    
    post_title = soup.find(class_='post-title')
    if post_title is not None:
        return post_title.text, 'post_title'
    
    div_post_headline = soup.find('div', {'class':'post-headline'})
    if div_post_headline is not None:
        return div_post_headline.text, 'div_post_headline'
    
    div_post_header = soup.find('div', {'class':'post-header'}) 
    if div_post_header is not None:
        if div_post_header.h1 is not None: 
            return div_post_header.h1.text, 'div_post_header1'
        if div_post_header.h2 is not None: 
            return div_post_header.h2.text, 'div_post_header2'

    posttitle = soup.find(class_='posttitle')
    if posttitle is not None:
        return posttitle.text, 'posttitle'
    
    the_title = soup.find(class_='the-title')
    if the_title is not None:
        return the_title.text, 'the_title'
    
    storycontent = soup.find('div', {'class':'storycontent'})    
    if storycontent is not None:
        return storycontent.a.text,'storycontent'

    span_title = soup.find('span', {'class':'title'})    
    if span_title is not None:
        return span_title.text, 'span_title'
    
    uk_article_title = soup.find(class_='uk-article-title')    
    if uk_article_title is not None:
        return uk_article_title.text, 'uk_article_title'
    
    entry_header = soup.find(class_='entry-header')    
    if entry_header is not None:
        return entry_header.text, 'entry_header'
    
    h_titles = soup.find(class_='titles')    
    if h_titles is not None:
        return h_titles.a.text, 'h_titles'
    
    h2_top = soup.find('div',{'class':'content'}) #anhonestclimatedebate
    if h2_top is not None:
        return h2_top.h2.text, 'h2_top'
    
    return None, 'none'

#def title_from_bold_content(soup):
    


        

def get_author(soup):
    a_author = soup.find('a', {'class':'author'}) #watts
    post_author = soup.find('span', {'class':'post-author'}) #motls
    author_name = soup.find('span', {'class':'author-name'}) 
    if a_author is not None:
        author = a_author.text
    elif post_author is not None:
        author = post_author.text
    
 
    
    
    author_tag = soup.find('a', {'rel':'author'})

    
def get_pubtime(soup):
    title_tag = soup.find('meta', {'property':'article:published_time'}) #get the content
    title_tag = soup.find_all(class_='date-header') #motls
    author_tag = soup.find('a', {'class':'timestamp-link'}) #motls
    author_tag = soup.find('abbr', {'class':'published'}) #motls



def get_body(soup):
    author_tag = soup.find('div', {'class':'entry-content'}) #watts
    author_tag = soup.find('div', {'class':'post-body'}) #motls

    


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('climateblog_metadata')

s3 = boto3.client('s3')

response = table.scan(Limit=5000)
items = response['Items']

df = pd.DataFrame(columns=['url','content','download_time', 'uuid','homepage'],index=range(0,100))

for i, item in enumerate(items):
    df.loc[i, 'uuid'] = item['uuid']
    df.loc[i, 'download_time'] = item['download_time']
    df.loc[i, 'url'] = item['url']
    df.loc[i, 'homepage'] = item['homepage']
    df.loc[i, 'content'] = s3.get_object(Bucket='climateblogs', Key=item['uuid'])['Body'].read()

df.to_pickle('feature_extract_toy.pkl')


df['title'] = ''

df['tag_function'] = ''

for i in range(0,len(df)):
    soup = make_soup(df.loc[i, 'content'])
    df.loc[i, 'title'], df.loc[i,'tag_function'] = scan_for_title_tags(soup)
    