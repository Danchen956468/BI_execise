

import os
import sys
import numpy
import random
import datetime
from weather import Weather,Unit

def print_hello(i,date,number):
    try:
       print("%d-th,date:%s,number:%d"%(i,str(date),number))

    except Exception as e:
       print(e)

if __name__=="__main__":
   date=datetime.datetime.now()
   for i in range(10):
       rdnumber=random.randint(1,100)
       print_hello(i,date,rdnumber)

