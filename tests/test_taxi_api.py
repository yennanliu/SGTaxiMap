import pytest, unittest
import sys
sys.path.append(".") 
from controller import Taxi

taxi = Taxi()

def test_call_taxi_api():
    result, response = taxi.call_taxi_api()
    assert response.code == 200 

def test_taxi_data_type():
    result, response = taxi.call_taxi_api()
    assert type(result) == dict  

def test_taxi_data_not_null():
    result, response = taxi.call_taxi_api()
    assert len(result['features'][0]['geometry']['coordinates']) > 0 

if __name__ == '__main__':
    pytest.main([__file__])