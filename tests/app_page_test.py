import sys
import requests
import json
import pytest

def test_helloworld():
    response = requests.get('http://0.0.0.0:5000/hello_world')
    assert response.status_code == 200

def test_main_page():
    response = requests.get('http://0.0.0.0:5000/')
    print (response)
    assert response.status_code == 200

if __name__ == "__main__":
    test_helloworld()
    test_main_page()