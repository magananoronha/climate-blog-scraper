#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:42:17 2017

@author: magananoronha
"""

import pandas as pd

df = pd.read_pickle('../data/postgres_db.pkl')

mismatch_bool = [y in x for x, y in zip(df['url'], df['blog_url'])]

flip = [not i for i in mismatch_bool]

tmp = df[flip]


blog_posts = df[df.blog_url == 'https://www.thegwpf.com/']