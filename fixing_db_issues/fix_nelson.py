#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:16:11 2017

@author: magananoronha
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:24:58 2017

@author: magananoronha
"""
from time import sleep
import boto3
import pandas as pd

if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('climateblog_metadata')

    client = boto3.client('s3')

    df = pd.read_pickle('to_delete.pkl')

    for i in range(len(df)):
        sleep(1)
        print(i)
        client.delete_object(Bucket='climateblogs', Key=df.iloc[i]['uuid'])
        table.delete_item(Key={'url': df.iloc[i]['url']})