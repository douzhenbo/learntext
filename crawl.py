import requests
from bs4 import BeautifulSoup


r=requests.get("http://www.baidu.com")
if r.status_code==200:
	print(r.text)
	r.encoding=r.apparent_encoding
	print(r.text)
