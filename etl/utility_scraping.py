#!/usr/bin/env python


import datetime
import pandas as pd
import numpy as np
import sys
import os
import urllib, json
import datetime as dt 



def get_lon_lat():
	request_headers = {"api-key": "gWpVyvnoSuAeW1J27L7W4nNG4gbQwfVC"}
	request = urllib.request.Request('https://api.data.gov.sg/v1/transport/taxi-availability',headers=request_headers)
	response = urllib.request.urlopen(request)
	assert response.code == 200
	result = json.loads(response.read().decode('utf-8'))
	(json.loads(json.dumps(result, ensure_ascii=False)))
	data = result['features'][0]['geometry']['coordinates']
	df = pd.DataFrame(result['features'][0]['geometry']['coordinates'])
	df.columns = ['lon', 'lat']
	df['timestamp']=dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
	#print (df)
	return  df



#if __name__ == '__main__':
#	get_lon_lat()









