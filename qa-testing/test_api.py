import requests
import pytest
def test_baidu_homepage():
    url = "https://www.baidu.com"
    response=requests.get(url,timeout=5)
    assert response.status_code==200
def test_baidu_404():
    url="https://www.baidu.com/this_page_does_mot_exist_123"
    response=requests.get(url,timeout=5)
    assert response.status_code==404
