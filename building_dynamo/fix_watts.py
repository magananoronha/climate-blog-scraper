#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:00:37 2017

@author: magananoronha

Some of my early wattsupwiththat posts had a different homepage url.

Successuflly ran the script.  All is well.

Modified the script to fix an issue with the wrong homepage url in realclimate posts.
"""

import boto3
from time import sleep
import pickle
from boto3.dynamodb.conditions import Attr


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('climateblog_metadata')

response = table.scan(
    FilterExpression=Attr('homepage').eq('http://www.climatedepot.com/') & Attr('url').begins_with('https://realclimatescience.com/')
)

items = response['Items']

while True:
    sleep(4)
    if response.get('LastEvaluatedKey'):
        
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'],
                              FilterExpression=Attr('homepage').eq('http://www.climatedepot.com/') & Attr('url').begins_with('https://realclimatescience.com/'))
        print(len(response['Items']))
        items = response['Items']
        for item in items:
            sleep(1)
            table.update_item(
                Key={
                    'url': item['url'],
                },
                UpdateExpression='SET homepage = :val1',
                ExpressionAttributeValues={
                    ':val1': 'https://realclimatescience.com/'
                })        
    else:
        break



    
with open('problem_watts.pkl', 'wb') as fp:
    pickle.dump(items, fp)
