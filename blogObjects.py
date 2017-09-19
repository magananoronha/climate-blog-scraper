#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:26:39 2017

@author: magananoronha
"""

from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import datetime
import random
import boto3

class StandardWordpress:
    
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
        if entry_title is not None:
            return entry_title.text   
        else:
            return None
    
    
    def get_prev(self, soup):
        a_prev = soup.find('a', {'rel':'prev'})
        if a_prev is not None:
            return a_prev['href']   
        else:
            return None        


    def get_next(self, soup):
        a_next = soup.find('a', {'rel':'next'})
        if a_next is not None:
            return a_next['href'] 
        else:
            return None  
        
    
    def get_body(self, soup):
        body_text = ''
        body = soup.find('div', {'class':'entry-content'})
        if body is not None:
            body = body.find_all('p')
            for element in body:
                body_text += ''.join(element.findAll(text = True))
            return body_text
        else:
            return None
    
    
    def get_pubtime(self, soup):
        pub_time = soup.find('meta', property='article:published_time')
        if pub_time is not None:
            return pub_time['content']
        time_class = soup.find(class_='entry-date')
        if time_class is not None:
            if 'datetime' in time_class.attrs.keys():
                return time_class['datetime']
            else:
                return time_class.text
        abbr_pub = soup.find('abbr', {'class':'published'})
        if abbr_pub is not None:
            if 'title' in abbr_pub.attrs.keys():
                return abbr_pub['title']
            else:
                return abbr_pub.text            
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
        if entry_title is not None:
            return entry_title.text     
        post_title = soup.find(class_='post-title')
        if post_title is not None:
            a_post = post_title.find('a') 
            if a_post is not None:
                return a_post.text
        entry_bold = soup.find(class_='entry-content')
        if entry_bold is not None:
            bold = entry_bold.find('b')
            if bold is not None:
                return bold.text
        else:
            return None

        
    def get_prev(self, soup):
        a_pager_older = soup.find('a', {'class':'blog-pager-older-link'})
        if a_pager_older is not None:
            return a_pager_older['href']   
        else:
            return None        
        
        
    def get_next(self, soup):
        a_pager_newer = soup.find('a', {'class':'blog-pager-newer-link'})
        if a_pager_newer is not None:
            return a_pager_newer['href'] 
        else:
            return None  
        
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-content'})
        if body is not None:
            return body.text
        post_body = soup.find('div', {'class':'post-body'})
        if post_body is not None:
            body = post_body.find_all('p')
            body_text = ''
            for element in body:
                body_text += ''.join(element.findAll(text = True))
            return body_text
        else:
            return None
    
    
    def get_pubtime(self, soup):
        pub_time = soup.find('abbr', {'class':'published'})
        if pub_time is not None:
            if 'title' in pub_time.attrs.keys():
                return pub_time['title']
            else:
                return pub_time.text
        entry_title = soup.find(class_='date-header')
        if entry_title is not None:
            return entry_title.text
        else:
            return None
        
        
        