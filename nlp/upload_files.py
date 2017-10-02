#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:37:06 2017

@author: magananoronha
"""

import boto3
import os


if __name__ == '__main__':

    data_directory = os.path.join('/home/ubuntu/workspace/climate-blog-scraper/data')
    word2vec_filepath = os.path.join(data_directory, 'word2vec_model_all')
    final_filepath = os.path.join(data_directory, 'final.txt')

    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(word2vec_filepath, 'climateblogs', 'blog2vec')
    s3.meta.client.upload_file(final_filepath, 'climateblogs', 'preprocessed_text.txt')