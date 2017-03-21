import requests
import time
import csv
from bs4 import BeautifulSoup

USERNAME = 'gong-chang-shao'
filename = '%s.csv' % (USERNAME)
offset = 0

headers = {
        'Cookie': 'd_c0="ABACeiPuKwuPTi544NVJjPTaS40_R6gz5LI=|1484706668"; _zap=a062f552-499f-4c8f-a261-09689401a4bd; login="MzBjZjMyYWYwZDY4NGIxZWEwNDI2M2E4OTM3Mzg0OWM=|1486496120|06ac1db6e293eb4d089706c963a1ca6891b798cf"; _xsrf=01e512bb5c689ec22209b1e6f4e480f4; q_c1=02d871bad1b6434086fe737982df2a3d|1487334669000|1484706667000; capsion_ticket="2|1:0|10:1488118101|14:capsion_ticket|44:YTJmZmJkZjgxZDRkNDMyMjgyYmExYTRiOGI0MGViMzQ=|a2062195ba6dbec3966b6330adf194956de0530140cbbea3e7268c450e8e38a8"; cap_id="YjNjYmJmZDhjYTljNDg5OWFiZjUxODVhZjNhNzg0MzQ=|1488118104|dcdaac05d9812f828b138753c6f4d8a1ee1de423"; l_cap_id="OTc1Zjc5YTBmM2Y3NDQ0Y2E2NTJkODYwOTRmNDZhZTg=|1488118104|f6806a6483de467f42e1fa9a9499bf468ffe203d"; nweb_qa=heifetz; aliyungf_tc=AQAAABhu0l2bXAcArUUgd5Q4rHziy6ti; __utma=51854390.1439269847.1488033758.1488332742.1488336624.17; __utmb=51854390.0.10.1488336624; __utmc=51854390; __utmz=51854390.1488016023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1; z_c0=Mi4wQUFEQTBzY2VBQUFBRUFKNkktNHJDeGNBQUFCaEFsVk5XbTdhV0FCVEF6bDdzV2lWM3kwUW9XaFhKMG9LbDdpckRn|1488336628|6e6d547452bad801110bdc1b0695e031e7b9f722',
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


