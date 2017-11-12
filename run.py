from flask import Flask, render_template, redirect, url_for, request
import csv
from controller import taxi

app = Flask(__name__)



@app.route('/')
def test():
    stop_list = taxi()
    print (stop_list)
    return render_template('taxi.html',stop_list=stop_list) 



@app.route('/dev1')
def test1():
   
    return render_template('dev1.html') 








if __name__ == '__main__':
   app.run(host='0.0.0.0')
