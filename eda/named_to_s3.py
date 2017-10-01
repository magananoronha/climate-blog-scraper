#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:57:10 2017

@author: magananoronha
"""

from io import StringIO
import boto3
import pandas as pd


if __name__ == '__main__':
    df = pd.read_pickle('name.pkl')
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object('climateblogs', 'df.csv').put(Body=csv_buffer.getvalue())