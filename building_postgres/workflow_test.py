#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 12:27:42 2017

@author: magananoronha

The entire contents of scraped blogs is being stored in an S3 bucket, with 
file metadata stored in a DynamoDB table.

Built Python classes for each blog that extracts structured data from 
S3 files.  

Goal if this script is to test scripting the process of getting file from S3,
extracting data with classes, and inserting data into Postgres
"""

