#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:24:43 2017

@author: magananoronha
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

currently_running = pd.read_csv('blog_links.csv')
all_blogs = pd.read_csv('homepages.csv')
attempted = pd.read_csv('blog_links_mod.csv')

all_blogs.drop(['Unnamed: 0'], axis=1, inplace=True)
