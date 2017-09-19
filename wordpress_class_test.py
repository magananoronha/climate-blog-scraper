#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:24:00 2017

@author: magananoronha
"""

import pandas as pd
import random

df = pd.read_pickle('feature_extract_toy.pkl')
df = pd.DataFrame(df)


site_list = df.groupby('homepage').apply(lambda x :x.iloc[random.choice(range(0,len(x)))])
site_list.reset_index(drop=True, inplace=True)
#post_count = df.groupby('homepage').count()
#
#site_list = site_list['homepage']
#
#site_list.to_csv('site_list.csv')
#   
title_list = []
body_list = []
pub_list = []
next_post_list = []
prev_post_list = []
pub_time_list = []

df = site_list

for i in range(0,len(df)):
    tmp = StandardBlogspot(df.iloc[i]['content'])
    title_list.append(tmp.title)
    body_list.append(tmp.body)
    pub_list.append(tmp.pub_time)
    next_post_list.append(tmp.next_post)
    prev_post_list.append(tmp.prev_post)
    pub_time_list.append(tmp.pub_time)


df['title'] = title_list
df['body'] = body_list
df['prev_post'] = next_post_list
df['next_post'] = prev_post_list
df['pub_time'] = pub_time_list


look = df.drop(['content'],axis=1)
look['post_len'] = [len(x) if x is not None else 0 for x in look.body]

std_bsp = df[(df.title).notnull() & (df.body).notnull() & (df.pub_time).notnull() & (df.next_post).notnull() & (df.prev_post).notnull()]
std_bsp['class'] = 'StandardBlogspot'

std_wp = pd.concat([std_wp.homepage, std_wp['class']], axis=1)

std_wp.to_csv('standard_wordpress.csv')

#wordpress = pd.read_csv('modernwordpress.csv')