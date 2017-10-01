#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:40:07 2017

@author: magananoronha

Accesses Postgres DB on AWS RDS.  Creates tables and populates the blog table.

Blog table has the blog homepage and the name of the python class that extracts
the data for the posts table.  

Populating the posts table is going to be some more work, will probably need
to be run on an EC2 instance.  
"""

import psycopg2
import pandas as pd

with open('db_schema.sql') as f:
    create_tables = f.read()
     
conn = psycopg2.connect(database='testdb', user='magananoronha', password="Play12it",
    host='testdb.cvslli4tn2ay.us-west-2.rds.amazonaws.com', port='5432',
    connect_timeout=10)
    
#conn = psycopg2.connect(database='testdb', user='postgres')

cursor = conn.cursor()


cursor.execute(create_tables)


blog_vals = pd.read_csv('classNames.csv')

pop_blog_table = ''
leader = 'INSERT INTO blogs (url, cleaning_class) VALUES'

for i in range(len(blog_vals)):
    insert_row = "('{}', '{}');\n".format(blog_vals.iloc[i]['homepage'], blog_vals.iloc[i]['className'])
    pop_blog_table = pop_blog_table + leader + insert_row
    
cursor.execute(pop_blog_table)

conn.commit()


cursor.execute('SELECT * FROM blogs;')