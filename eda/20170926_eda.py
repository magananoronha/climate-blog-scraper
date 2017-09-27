#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:18:08 2017

@author: magananoronha

Finished moving data into PostgresDB.  Did a select * on the post table
and saved it as a pickle file locally.  Doing some first pass EDA on the data.
"""

import pandas as pd
import numpy as np

data = pd.read_pickle('../data/postgres_sample.pkl')
df = pd.DataFrame(data, columns=['url','uuid','download_time','blog_url','title','author','pub_time','body'])
df['word_count'] = [len(x.split()) if x is not None else 0 for x in df.body]

