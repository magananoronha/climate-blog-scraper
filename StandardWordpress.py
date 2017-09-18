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
        self.author = self.get_author(soup)
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

        
    def get_author(self, soup):
        a_author = soup.find('a', {'class':'author'})
        if a_author is not None:
            return a_author.text 
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
        pub_time = soup.find('meta', {'property':'article:published_time'})
        if pub_time is not None:
            return pub_time.content
        else:
            return None

    