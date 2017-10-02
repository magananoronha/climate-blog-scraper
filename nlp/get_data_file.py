#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:23:29 2017

@author: magananoronha
"""

import boto3
import botocore
import os

if __name__ == '__main__':
    s3 = boto3.resource('s3')
    
    BUCKET_NAME = 'climateblogs' # replace with your bucket name
    KEY = 'cleaned_db.pkl' # replace with your object key
        
    data_directory = '/home/ubuntu/workspace/climate-blog-scraper/data'
    filepath = os.path.join(data_directory,KEY)        

    
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, filepath)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
