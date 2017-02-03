import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/people/gong-chang-shao/followers?page=1'
headers_1 = {
        'Cookie': 'YOUR OWN COOKIE HERE',
        'Host':'www.zhihu.com',
        'Referer':'http://www.zhihu.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding':'gzip',
        'Connection': 'keep-alive'
    }

headers_2 = {
        'Cookie': 'YOUR OWN COOKIE HERE',
        'Host':'www.zhihu.com',
        'Referer':'http://www.zhihu.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding':'gzip',
        'Connection': 'keep-alive'
    }

      
# The reason why always get only first three item is because the retreived html is directly from server side and
# not processed by javacript yet.
'''
re = requests.get(url, headers=headers_2)
soup = BeautifulSoup(re.text, 'lxml')

item = soup.findAll('div', attrs={'class': 'List-item'})
print(item)
print(type(item))
'''




g = ('https://www.zhihu.com/api/v4/members/YOUR_NAME_HERE/followers'
     '?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count'
     '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)'
     '%5D.topics'
     '&offset=0'
     '&limit=20')
get = requests.get(g, headers=headers_1)

total_follower = get.json()['paging']['totals']
offset = 2550
while offset < total_follower:
    url = ('https://www.zhihu.com/api/v4/members/YOUR_NAME_HERE/followers'
           '?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count'
           '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)'
           '%5D.topics'
           '&offset={}'
           '&limit=20')

    res = requests.get(url.format(offset), headers=headers_1)
    print(res.json()['data'][0])
    print(type(res.json()['data'][0]))
    print(len(res.json()['data'][0]))
    offset += 20
    time.sleep(1)







    
    
