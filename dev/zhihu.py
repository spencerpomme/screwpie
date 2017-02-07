import requests
import time
import csv
from bs4 import BeautifulSoup

USERNAME = 'YOURNAME'
filename = '%s.csv' % (USERNAME)
offset = 0

headers = {
        'Cookie': 'YOUR COOKIE HERE',
        'Host':'www.zhihu.com',
        'Referer':'http://www.zhihu.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding':'gzip',
        'Connection': 'keep-alive'
    }

g = ('https://www.zhihu.com/api/v4/members/{}/followers'
     '?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count'
     '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)'
     '%5D.topics'
     '&offset=0'
     '&limit=20').format(USERNAME)

get = requests.get(g, headers=headers)

file = open(r'%s' % filename, 'w', newline='', encoding='utf8')
total_follower = get.json()['paging']['totals']
item_num = len(get.json()['data'])
print('total follower: %d' % total_follower)

file = open(r'%s' % filename, 'w', newline='', encoding='utf8')
writer = csv.writer(file)

while offset < total_follower:
    print('current offset: ', offset)
    url = ('https://www.zhihu.com/api/v4/members/{}/followers'
           '?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count'
           '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)'
           '%5D.topics'
           '&offset={}'
           '&limit=20')
    try:
        res = requests.get(url.format(USERNAME, offset), headers=headers)
    except Exception as e:
        print('exception at offset %d:' % offset)
        print(e)
        offset -= 20
        continue
    for i in range(item_num):
        try:
            cd = res.json()['data'][i]
            # Only selected some of the fields
            writer.writerow([cd['name'], cd['is_followed'], cd['is_following'], cd['url_token'],
                             cd['answer_count'], cd['follower_count'], cd['badge'] != []])
        except IndexError:
            pass
    offset += 20
    time.sleep(0.5)
print('done')
file.close()


