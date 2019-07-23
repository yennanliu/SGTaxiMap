import pytest, unittest 
from controller import call_taxi_api

def test_call_taxi_api():
	result, response = call_taxi_api()
	assert response.code == 200 

if __name__ == '__main__':
    pytest.main([__file__])