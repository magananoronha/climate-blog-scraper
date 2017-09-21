#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:24:58 2017

@author: magananoronha
"""

from time import sleep
import boto3
import pickle


if __name__ == '__main__':

    dynamodb = boto3.resource('dynamodb')
    new_table = dynamodb.Table('climateblog_metadata')
    old_table = dynamodb.Table('post_metadata')

    client = boto3.client('s3')

    response = old_table.scan()

    items = response['Items']

    while True:
        print(len(response['Items']))
        sleep(1)
        if response.get('LastEvaluatedKey'):
            response = old_table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response['Items']
        else:
            break

    with open('dynamo_table.pkl', 'wb') as fp:
        pickle.dump(items, fp)




    for item in items:
        check = new_table.get_item(Key={'url':item['url']})
        if 'Item' in check.keys():
            print('{} already in new table'.format(item['url']))
            client.copy(Bucket='possible-dupes',
                        CopySource={'Bucket':'climateblogs',
                                    'Key':item['uuid']},
                        Key=item['uuid']
                        )
            print('Copied {} S3 File'.format(item['uuid']))
            client.delete_object(Bucket='climateblogs', Key=item['uuid'])
            print('Deleted {} S3 File'.format(item['uuid']))
        else:
            print('{} not in new table'.format(item['url']))
            new_table.put_item(Item={
                    'url' : item['url'],
                    'uuid' : item['uuid'],
                    'homepage' : item['homepage'],
                    'download_time' : item['download_time']})
            print('Put {} in new table'.format(item['uuid']))
        old_table.delete_item(Key={'uuid': item['uuid']})
        print('Deleted {} from old table'.format(item['uuid']))
