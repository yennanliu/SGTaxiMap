import datetime
import pandas as pd
import numpy as np
import sys
import os
import urllib, json
import datetime as dt 

now = datetime.datetime.now()
date_ = now.strftime("%Y-%m-%d")

class save_output(object):

  def __init__(self, df):
    self.df = df

  def save_user_profile(self):
    try:
      self.df.to_csv('output/SG_taxi_{}.csv'.format(date_))
      print ('Succefully save taxi location data  to /output at {}'.format(date_))
    except Exception as e:
      print ('Save failed') 
      print (e)

  def save_user_profile_DB(self):
    try:
      import sqlite3
      conn = sqlite3.connect("output/SG_taxi.db")
      self.df.to_sql("taxi", conn, if_exists="append")
      print ('Succefully save taxi location data as sqlite db to /output at {}'.format(date_))
    except Exception as e:
      print ('Save failed') 
