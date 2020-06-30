import requests
from bs4 import BeautifulSoup

with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

import urllib.request
import urllib.parse

with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

import requests

# web_url에 원하는 웹의 URL을 넣어주시면 됩니다.
>>> r = requests.get(web_url)
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.encoding
'UTF-8'
>>> r.text
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">













def crawler():
    url = 'https://www.google.com'
    html = requests.get(url)
    print(html.text)


crawler()

