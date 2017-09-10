"""
Created on Sat Sep  9 16:20:39 2017

@author: magananoronha
"""
import pickle
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import requests
import numpy as np
import re

df = pd.read_pickle('first_page.pkl')

def grab_first_page(df):
    df['page_content'] = ''
    for index, row in df.iterrows():
        if (df.loc[index, 'page_content'] == '') and (type(df.loc[index, 'recent_post']) == str):
            df.loc[index, 'page_content'] = requests.get(df.loc[index, 'recent_post']).content


def check_for_tags(df):
    for index in range(0, len(df)):
        soup = BeautifulSoup(df.loc[index, 'page_content'], 'lxml')
        if len(soup.findAll('div', {'class':'nav-previous'})) > 0:
            df.loc[index, 'div_class=nav-previous'] = 1
        if len(soup.findAll('link', {'rel':'prev'})) > 0:
            df.loc[index, 'link_rel=prev'] = 1
        if len(soup.findAll('a', {'rel':'prev'})) > 0:
            df.loc[index, 'a_rel=prev'] = 1
        if len(soup.findAll('a', {'class': 'blog-pager-older-link'})) > 0:
            df.loc[index, 'prev_tag'] = 'a, class:blog-pager-older-link'
        elif len(soup.findAll('a', {'class':'journal-entry-navigation-next'})) > 0:
            df.loc[index, 'prev_tag'] = 'a, class:journal-entry-navigation-next'
        elif len(soup.findAll('a', {'class':'snippet-fade'})) > 0:
            df.loc[index, 'prev_tag'] = 'a, class:snippet-fade'

def print_href(df):
    for index in range(0, len(df)):
        if df.loc[index, 'prev_tag'] == 'div, class:nav-previous':
            soup = BeautifulSoup(df.loc[index, 'page_content'], 'lxml')
            link = soup.find('a', {'rel':'prev'})
            print(link['href'])


df['a_rel=prev'] = 0
df['link_rel=prev'] = 0
df['div_class=nav-previous'] = 0


grab_first_page(df)
check_for_tags(df)

df.to_pickle('first_page.pkl')

df.drop(['page_content'],axis=1,inplace=True)

no_tag = df[df.prev_tag == '']

df['a_rel=prev'].sum()
df['link_rel=prev'].sum()
df['div_class=nav-previous'].sum()