import sys
import requests
import json
import pytest

#sys.path.append("..")
#from config import domain as dm

# def test_index():
#     url = dm.DOMAIN[dm.type] + '/'
#     print (url)
#     r = requests.get(url)
#     res = json.loads(r.text)
#     assert res['msg'] == "Hello World!"

#@pytest.fixture
def test_dummy():
    response = requests.get('http://0.0.0.0:5000/hello_world')
    assert response.status_code == 200

def test_get_taxi_location():
    url = 'http://0.0.0.0:5000/'
    print (url)
    response = requests.get(url)
    print (response)
    assert  response.status_code == 200

if __name__ == "__main__":
    #test_index()
    test_dummy()