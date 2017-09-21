#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:00:37 2017

@author: magananoronha

Some of my early wattsupwiththat posts had a different homepage url.

Successuflly ran the script.  All is well.
"""

import boto3
from time import sleep
import pickle
from boto3.dynamodb.conditions import Attr


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('climateblog_metadata')

response = table.scan(
    FilterExpression=Attr('homepage').eq('wattsupwiththat.com')
)

items = response['Items']

while True:
    print(len(response['Items']))
    sleep(4)
    if response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'],
                              FilterExpression=Attr('homepage').eq('wattsupwiththat.com'))
        items += response['Items']
    else:
        break


for item in items:
    sleep(4)
    table.update_item(
        Key={
            'url': item['url'],
        },
        UpdateExpression='SET homepage = :val1',
        ExpressionAttributeValues={
            ':val1': 'https://wattsupwiththat.com/'
        }
    )
    
with open('problem_watts.pkl', 'wb') as fp:
    pickle.dump(items, fp)
