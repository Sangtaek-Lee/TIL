from urllib import response
import requests
from bs4 import BeautifulSoup

# 1. 주소
URL = 'https://www.naver.com/'
# 2. 요청
#
# response (200) : 성공적으로 가져왔다! <=> 404, 500
response = requests.get(URL)
print(response, type(response))     #객체다?

response = requests.get(URL).text
print(response, type(response))     #string이다

# 2-1. BeatifulSoup (text -> 다른 객체)

data = BeautifulSoup(response, 'html_parser')
print(data)
print(type(data), type(response))