from flask import Flask, render_template, redirect, url_for, request
from controller import taxi
import csv

app = Flask(__name__)

@app.route('/')
def test():
    stop_list = taxi()
    print (stop_list)
    return render_template('taxi.html',stop_list=stop_list) 

@app.route('/dev1')
def test1():
	# hard code taxi_count for dev
	taxi_count = 1000
	print (taxi_count)
	# render taxi_count value to html 
	return render_template('dev1.html', taxi_count=taxi_count) 

if __name__ == '__main__':
   app.run(host='0.0.0.0')
