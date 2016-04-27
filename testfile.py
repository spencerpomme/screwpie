import requests, bs4
url = 'http://www.douban.com/group/yuexiuzufang/discussion?start=0'
url2 = 'http://www.baidu.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
           "Connection": "keep-alive",
           }
proxies = {'http':'http://192.99.246.183:9000'}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.status_code)
print(response.request.headers)
