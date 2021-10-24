# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:19:01 2021

@author: Lenovo
"""

import vertica_python as vp
import pandas as pd

conn_info = {'host': 'localhost:5433',
         'user': 'dbadmin',
         'password': '',
         'database': 'VMart'}

file = "D://studying//3 year//genesis//1//sandbox.KNU//product//users.tsv"


df = pd.read_csv(file, sep='\t')

lists = df.values.tolist()

#connection = vp.connect(host = '5433',user = 'dbadmin', password = '',database = 'VMart')

#with connection.cursor() as cursor:
for x in lists[0:10]:
       # cursor.execute("insert into test values (%s,%s)" , x)
        #connection.commit()
        print(x)
        
        