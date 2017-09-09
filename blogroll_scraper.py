from bs4 import BeautifulSoup
import os
from PIL import Image
import requests
from time import sleep

urls = []
with open('blogs.csv', 'r') as f:
    for line in f:
        urls.append(line.strip('\n'))


def get_blogroll(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content)

    blogroll = soup.findAll(class='xoxo blogroll')


soup = get_soup(url)
title = soup.findAll(class='entry-title')
date = soup.findAll(class='published')
content = soup.findAll(class='entry-content')
url = soup.findAll(class='nav-previous')
