#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:02:11 2017

@author: magananoronha
"""

import boto3
import botocore
import pandas as pd
from time import sleep
import uuid

df = pd.read_pickle('20170910_wattsup_test.pkl')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('post_metadata')

s3 = boto3.resource('s3')

for index in range(0,len(df)):
    post_uuid = str(uuid.uuid4())
    s3.Bucket('climateblogs').put_object(Key=post_uuid, Body=df.loc[index,'content'].encode())
    table.put_item(Item={
            'uuid' : post_uuid,
            'url' : df.loc[index, 'url'],
            'homepage' : 'wattsupwiththat.com',
            'download_time' : df.loc[index, 'download_time'].strftime("%Y-%m-%d %X")})
    print(index)


