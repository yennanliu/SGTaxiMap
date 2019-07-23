from flask import Flask, render_template, redirect, url_for, request
from controller import taxi
import csv

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return "hello world", 200 

@app.route('/')
def get_taxi_location():
    stop_list = taxi()
    print (stop_list)
    return render_template('taxi.html',stop_list=stop_list), 200 

@app.route('/dev_page')
def get_taxi_location_dev():
	# hard code taxi_count for dev
	taxi_count = 1000
	print (taxi_count)
	# render taxi_count value to html 
	return render_template('dev_page.html', taxi_count=taxi_count), 200 

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
