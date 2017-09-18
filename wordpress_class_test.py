#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:24:00 2017

@author: magananoronha
"""

import pandas as pd
import random

df = pd.read_pickle('feature_extract_toy.pkl')

df = df.groupby('homepage').apply(lambda x :x.iloc[random.choice(range(0,len(x)))])
df.reset_index(drop=True, inplace=True)

   
title_list = []
author_list = []
body_list = []
pub_list = []

for i in range(0,len(df)):
    tmp = StandardWordpress(df.iloc[i]['content'])
    title_list.append(tmp.title)
    author_list.append(tmp.author)
    body_list.append(tmp.body)
    pub_list.append(tmp.pub_time)

df['title'] = title_list
df['author'] = author_list
df['body'] = body_list
df['pub_time'] = pub_list
