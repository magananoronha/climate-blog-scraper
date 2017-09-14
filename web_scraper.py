#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:32:36 2017

@author: magananoronha

First iteration of webscraper, tested by scraping 50 blog posts from 
Watts Up With That.  
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
import datetime
import random


df = pd.read_pickle('20170910_wattsup_test.pkl')


def download_page(df, url, index):
    df.loc[index,'download_time'] = datetime.datetime.now()
    df.loc[index,'url'] = url
    df.loc[index,'content'] = requests.get(url).content
    soup = BeautifulSoup(df.loc[index,'content'],'lxml')
    link = soup.find('link', {'rel':'prev'})
    new_url = link['href']
    return new_url

        
if __name__ == '__main__':
    url = 'https://wattsupwiththat.com/2017/09/10/lse-bob-ward-hurricanes-are-president-trumps-fault/'
    df = pd.DataFrame(columns=['url','content','download_time'],index=range(0,50))
    
    for index in range(0,len(df)):
        url = download_page(df, url, index)
        sleep(random.randint(60,120))
    
    df.to_pickle('20170910_wattsup_test.pkl')