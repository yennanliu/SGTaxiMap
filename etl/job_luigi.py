#!/usr/bin/env python

import luigi

import datetime
import pandas as pd
import numpy as np
import sys
import os


from utility_scraping import *
from utility_IO import *



class demo_task(luigi.Task): 
    def my_first_task():
        print ('==============')
        print ('first task')
        print ('==============')
    def my_second_task():
        print ('==============')
        print ('2nd task')
        print ('==============')
    def run(self):
        demo_task.my_first_task()
        demo_task.my_second_task()



class Agg_taxi_locations(luigi.Task):
	def get_locations():
		df = get_lon_lat()
		print (df.head())
	def run(self):
		Agg_taxi_locations.get_locations()




if __name__ == '__main__':

    luigi.run( )
