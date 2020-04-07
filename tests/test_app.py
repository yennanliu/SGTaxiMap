import sys
import requests
import json
import pytest
import sys
sys.path.append(".")
from run import app 

def test_helloworld():
    with app.test_client() as c:
        response = c.get('/hello_world')
        assert response.status_code == 200

def test_main_page():
    with app.test_client() as c:
        response = c.get('/')
        assert response.status_code == 200

def test_dev_page():
    with app.test_client() as c:
        response = c.get('/dev_page')
        assert response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__])