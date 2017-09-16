#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:24:43 2017

@author: magananoronha

Ran the scraper overnight last night, and most of this AM.  A lot of the blogs
have already been entirely scraped (28 as of writing).  

Checking in on what's been scraped and finding non-wordpress blogs that have 
a consistent tag system to add to scraper.  Found 22 blogspot blogs to add to scraper.

Added a few other blogs.  There's about 12 more that probably need to be scraped, 
but will require so more care.  Going to proceed without them for now.
"""

from bs4 import BeautifulSoup
import requests
from time import sleep
import pandas as pd
import datetime
import random
import boto3
import uuid
import numpy as np

tag_check = pd.read_pickle('first_page.pkl')

currently_running = pd.read_csv('blog_links.csv')
currently_running = currently_running.where((pd.notnull(currently_running)), None)

all_blogs = pd.read_csv('homepages.csv')
all_blogs.drop(['Unnamed: 0'], axis=1, inplace=True)
blog_set = set(all_blogs['homepage'])

attempted = pd.read_csv('blog_links_mod.csv')
attempted_set = set(attempted['homepage'])

not_attempted = list(blog_set - attempted_set)

stopped_running = currently_running[currently_running.recent_post.isnull()]
currently_running = currently_running[currently_running.recent_post.notnull()]

tags_not_attempt = tag_check[tag_check.homepage.isin(not_attempted)]
tags_not_attempt.drop(['page_content'], axis=1, inplace=True)

to_attempt = tags_not_attempt[tags_not_attempt.prev_tag == 'a, class:blog-pager-older-link']

new = pd.concat([to_attempt.homepage, to_attempt.recent_post],axis=1)

new_runlist = pd.concat([new, currently_running])

#new_runlist.to_csv('mix_links.csv', index=False)

still_not_attempted = blog_set - attempted_set - set(new['homepage'])

tags_still = tag_check[tag_check.homepage.isin(still_not_attempted)]
tags_still.drop(['page_content'], axis=1, inplace=True)


more_to_try = tags_still[(tags_still.platform != 'wordpress') & (tags_still.platform != 'blogspot')]
more_to_try = pd.concat([more_to_try.homepage, more_to_try.recent_post], axis=1)
more_to_try.drop([66,91], axis=0, inplace=True)
