#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:00:37 2017

@author: magananoronha

Some of my early wattsupwiththat posts had a different homepage url.

Successuflly ran the script.  All is well.

Have been editing this script as I need to make queries and changes to the dynamo db
"""

import boto3
from time import sleep
import pickle
import pandas as pd
import re
from boto3.dynamodb.conditions import Attr


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('climateblog_metadata')

response = table.scan(
    FilterExpression=Attr('homepage').eq('http://www.timworstall.com/')
)

items = response['Items']


while True:
    print(len(response['Items']))
    sleep(2)
    if response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'],
                              FilterExpression=Attr('homepage').eq('http://www.climatedepot.com/'))
        items += response['Items']
    else:
        break
    
df = pd.DataFrame(items)
df['date'] = [re.findall('.com/(\d{4}/\d{2}/\d{2})', x)[0] for x in df.url]
df['date'] = pd.to_datetime(df['date'])
    


#for item in items:
#    sleep(4)
#    table.update_item(
#        Key={
#            'url': item['url'],
#        },
#        UpdateExpression='SET homepage = :val1',
#        ExpressionAttributeValues={
#            ':val1': 'https://wattsupwiththat.com/'
#        }
#    )
#    
#with open('problem_watts.pkl', 'wb') as fp:
#    pickle.dump(items, fp)
