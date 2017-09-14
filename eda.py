"""
Created on Sat Sep  9 16:20:39 2017

@author: magananoronha
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

df = pd.read_pickle('first_page.pkl')
pages = pd.read_csv('homepages.csv')

new_pages = [x for x in pages.homepage if x not in set(df.homepage)]
pages = pages[pages.homepage.isin(new_pages)]
pages.drop(['Unnamed: 0'],axis=1,inplace=True)

pages['page_content'] = ''

df = df.append(pages)
df.reset_index(inplace=True,drop=True)

def grab_first_page(df):
    for index, row in df.iterrows():
        if (df.loc[index, 'page_content'] == '') and (type(df.loc[index, 'recent_post']) == str):
            df.loc[index, 'page_content'] = requests.get(df.loc[index, 'recent_post']).content


def check_for_tags(df):
    df['link_rel=prev'] = 0
    df['div_class=nav-previous'] = 0
    df['a_rel=prev'] = 0
    df['a_rel=prev'] = 0
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


grab_first_page(df)
check_for_tags(df)

df.to_pickle('first_page.pkl')

df.drop(['page_content'],axis=1,inplace=True)


df['a_rel=prev'].sum()
df['link_rel=prev'].sum()
df['div_class=nav-previous'].sum()

check = df.isnull()
check.drop(['platform','homepage','recent_post'], axis=1, inplace=True)
df['sum'] = check.sum(axis=1)

no_tag = df[df['sum'] == 4]
