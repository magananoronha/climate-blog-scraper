#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:26:39 2017

@author: magananoronha
"""

from bs4 import BeautifulSoup
from dateutil.parser import parse
import re


class WordpressFormat:

    def __init__(self, content):
        self.content = content
        soup = self.make_soup()
        self.title = self.get_title(soup)
        if self.title:
            self.title = self.clean_title()        
        self.author = self.get_author(soup)
        if self.author:
            self.author = self.clean_author()        
        self.prev_post = self.get_prev(soup)
        self.next_post = self.get_next(soup)
        self.body = self.get_body(soup)
        if self.body:
            self.body = self.clean_body()
        self.pub_time = self.get_pubtime(soup)
        if self.pub_time:
            self.pub_time = self.format_date()

    def make_soup(self):
        return BeautifulSoup(self.content,'html.parser')
    

    def format_date(self):
        try:
            pub_date = parse(self.pub_time)
        except ValueError:
            pub_date = None
        return pub_date
        
        
    def clean_body(self):
        return " ".join(self.body.split())
    
    
    def clean_title(self):
        if len(self.title) > 255:
            return None        
        else:
            return " ".join(self.title.split())    
    
    def clean_author(self):
        if len(self.author) > 255:
            return None
        else:
            return " ".join(self.author.split())         
    
    
    def get_title(self, soup):
        title = soup.find(class_='entry-title')
        if title:
            return title.text
        title = soup.find(class_='page-title')
        if title:
            return title.text
        title = soup.find('title')
        if title:
            title_bar = re.findall('(.*)\|',title.text)
            if title_bar:
                return title_bar[0]
            else:
                return None
        else:
            return None        
        
    def get_author(self, soup):
        author = soup.find(class_='fn')
        if author:
            return author.text
        else:
            return None


    def get_prev(self, soup):
        prev_post = soup.find('a', {'rel':'prev'})
        if prev_post:
            return prev_post['href']
        prev_post = soup.find('link', {'rel':'prev'})
        if prev_post:
            return prev_post['href']
        else:
            return None


    def get_next(self, soup):
        next_post = soup.find('a', {'rel':'next'})
        if next_post:
            return next_post['href']
        next_post = soup.find('link', {'rel':'next'})
        if next_post:
            return next_post['href']
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
        body = soup.find(class_='entry')
        if body:
            return self.concat_body(body) 
        body = soup.find('div', {'class':'post'})
        if body:
             return self.concat_body(body)     
        else:
            return None


    def get_pubtime(self, soup):
        pub_time = soup.find('meta', property='article:published_time')
        if pub_time:
            return pub_time['content']
        pub_time = soup.find(class_='entry-date')
        if pub_time:
            if 'datetime' in pub_time.attrs.keys():
                return pub_time['datetime']
            else:
                return pub_time.text
        else:
            return None
        
        

class BlogspotFormat(WordpressFormat):


    def __init__(self, content):
        WordpressFormat.__init__(self,content)


    def get_title(self, soup):
        title = soup.find(class_='entry-title')
        if title:
            return title.text
        title = soup.find(class_='post-title')
        if title:
            title = title.find('a')
            if title:
                return title.text
        else:
            return None


    def get_prev(self, soup):
        prev_post = soup.find('a', {'class':'blog-pager-older-link'})
        if prev_post:
            return prev_post['href']
        prev_post = soup.find('link', {'rel':'prev'})
        if prev_post:
            return prev_post['href']        
        else:
            return None


    def get_next(self, soup):
        next_post = soup.find('a', {'class':'blog-pager-newer-link'})
        if next_post:
            return next_post['href']
        next_post = soup.find('link', {'rel':'next'})
        if next_post:
            return next_post['href']
        else:
            return None


    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-content'})
        if body:
            return body.text
        body = soup.find('div', {'class':'post-body'})
        if body:
            return self.concat_body(body)
        body = soup.find(class_='entry')
        if body:
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
        pub_time = soup.find(class_='date-header')
        if pub_time:
            return pub_time.text
        else:
            return None
        
