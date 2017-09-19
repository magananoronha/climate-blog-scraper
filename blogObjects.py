#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:26:39 2017

@author: magananoronha
"""

from bs4 import BeautifulSoup
from time import sleep
from dateutil.parser import parse
import pandas as pd
import datetime
import random
import boto3
import re


class WordpressFormat:

    def __init__(self, content):
        self.content = content
        soup = self.make_soup()
        self.title = self.get_title(soup)
        self.author = self.get_author(soup)
        self.prev_post = self.get_prev(soup)
        self.next_post = self.get_next(soup)
        self.body = self.get_body(soup)
        if self.body:
            self.body = self.clean_body()
        self.pub_time = self.get_pubtime(soup)
        if self.pub_time:
            self.pub_time = self.format_date()

    def make_soup(self):
        return BeautifulSoup(self.content,'lxml')
    

    def format_date(self):
        return parse(self.pub_time)
    
    
    def clean_body(self):
        return " ".join(sentence.split())
    

    def get_title(self, soup):
        entry_title = soup.find(class_='entry-title')
        if entry_title:
            return entry_title.text
        page_title = soup.find(class_='page-title')
        if page_title:
            return page_title.text
        else:
            return None


    def get_prev(self, soup):
        a_prev = soup.find('a', {'rel':'prev'})
        if a_prev:
            return a_prev['href']
        link_prev = soup.find('link', {'rel':'prev'})
        if link_prev:
            return link_prev['href']
        else:
            return None


    def get_next(self, soup):
        a_next = soup.find('a', {'rel':'next'})
        if a_next:
            return a_next['href']
        link_next = soup.find('link', {'rel':'next'})
        if link_next:
            return link_next['href']
        else:
            return None

    def concat_body(self, body):
        body_text = ''
        body = body.find_all('p')
        for element in body:
            body_text += ''.join(element.findAll(text = True))
        return body_text


    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-content'})
        if body:
            return self.concat_body(body)
        body = soup.find('div', {'class':'entry-summary'})
        if body:
            return self.concat_body(body)
        body = soup.find('section', {'class':'entry'})
        if body:
             return self.concat_body(body)
        body = soup.find('div', {'class':'entry-container'})
        if body:
             return self.concat_body(body)
        body = soup.find('div', {'class':'post-entry'})
        if body:
             return self.concat_body(body)
        else:
            return None


    def get_pubtime(self, soup):
        pub_time = soup.find('meta', property='article:published_time')
        if pub_time:
            return pub_time['content']
        time_class = soup.find(class_='entry-date')
        if time_class:
            if 'datetime' in time_class.attrs.keys():
                return time_class['datetime']
            else:
                return time_class.text
        abbr_pub = soup.find('abbr', {'class':'published'})
        if abbr_pub:
            if 'title' in abbr_pub.attrs.keys():
                return abbr_pub['title']
            else:
                return abbr_pub.text
        pub_time = soup.find('div', {'class':'post-box-meta-single'})
        if pub_time:
            spans = pub_time.find_all('span')
            if spans:
                return spans[-1].text
        pub_time = soup.find('div', {'class':'postmetadata'})
            if pub_time:
                return pub_time.text
        pub_time = soup.find('span', {'class':'author'})
        if pub_time:
            return pub_time.text
        pub_time = soup.find(class_='meta')
        if pub_time:
            li = pub_time.find('li')
            return li.text
        pub_time = soup.find('time')
        if pub_time:
            return pub_time['datetime']


        else:
            return None

class StandardBlogspot:


    def __init__(self, content):
        self.content = content
        soup = self.make_soup()
        self.title = self.get_title(soup)
        self.prev_post = self.get_prev(soup)
        self.next_post = self.get_next(soup)
        self.body = self.get_body(soup)
        self.pub_time = self.get_pubtime(soup)

    def make_soup(self):
        return BeautifulSoup(self.content,'lxml')


    def get_title(self, soup):
        entry_title = soup.find(class_='entry-title')
        if entry_title:
            return entry_title.text
        post_title = soup.find(class_='post-title')
        if post_title:
            a_post = post_title.find('a')
            if a_post:
                return a_post.text
        entry_bold = soup.find(class_='entry-content')
        if entry_bold:
            bold = entry_bold.find('b')
            if bold:
                return bold.text
        else:
            return None


    def get_prev(self, soup):
        a_pager_older = soup.find('a', {'class':'blog-pager-older-link'})
        if a_pager_older:
            return a_pager_older['href']
        else:
            return None


    def get_next(self, soup):
        a_pager_newer = soup.find('a', {'class':'blog-pager-newer-link'})
        if a_pager_newer:
            return a_pager_newer['href']
        else:
            return None

    def concat_body(self, body):
        body_text = ''
        body = body.find_all('p')
        for element in body:
            body_text += ''.join(element.findAll(text = True))
        return body_text


    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-content'})
        if body:
            return body.text
        post_body = soup.find('div', {'class':'post-body'})
        if post_body:
            return self.concat_body(body)
        else:
            return None


    def get_pubtime(self, soup):
        pub_time = soup.find('abbr', {'class':'published'})
        if pub_time:
            if 'title' in pub_time.attrs.keys():
                return pub_time['title']
            else:
                return pub_time.text
        entry_title = soup.find(class_='date-header')
        if entry_title:
            return entry_title.text
        else:
            return None

class ModifiedWordpress(StandardWordpress):
    def __init__(self, content):
        StandardWordpress.__init__(self,content)

    def first_bold_line(self, body):
        title = body.find(re.compile(r"^h\d$"))
        if title:
            return title.text

    def get_title(self, soup):
        entry_title = soup.find(class_='uk-article-title')
        if entry_title:
            return entry_title.text
        post_title = soup.find('div', {'class':'posttitle'})
        if post_title:
            return post_title.text
        post_title = soup.find('div', {'class':'post-headline'})
        if post_title:
            return post_title.text
        post_title = soup.find(class_='entry-header')
        if post_title:
            return post_title.text
        post_title = soup.find(class_='art-postheader')
        if post_title:
            return post_title.text
        post_title = soup.find(class_='titles')
        if post_title:
            return post_title.text
        body = soup.find('div', {'class':'post'})
        if body:
            return self.first_bold_line(body)
        body = soup.find('div', {'id':'content'})
        if body:
            return self.first_bold_line(body)
        body = soup.find('section', {'id':'content'})
        if body:
            return self.first_bold_line(body)
        else:
            return None
