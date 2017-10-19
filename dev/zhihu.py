import requests
import time
import csv
from bs4 import BeautifulSoup

USERNAME = 'gong-chang-shao'
filename = '%s.csv' % (USERNAME)
offset = 0

headers = {
        'Cookie':"d_c0=AADChMhkPQyPTiAmrWW-Hj4kUcVa9okWYx4=|1503058490;_zap=4e412ea7-7276-4e1c-87b8-014f7442b337;q_c1=9c24d364675c4ff7873021ca31179274|1505726518000|1503058489000;r_cap_id=Y2U0YmUxZGJjNDQyNDlmOTgxNjA2MGZlMWQyMTBjNTU=|1507465164|83c7876186eab6468238b8f1a6aa440fdbf19424;cap_id=OWU0NDczZmJiNmJhNGJjZGEzNTM4NTc1NWI1MjQ0OWY=|1507465164|6719184908a72aeffeacaff0ea80d5db9c811001;capsion_ticket=2|1:0|10:1507465200|\
        14:capsion_ticket|44:ZmY5NTcyZDZiMTc5NGRlNzk1OTI1M2RhMTRhOWM1YjE=|e69e7b0848fc9fb071462ecfc2e2ac6c4449557ebd1d3;l_cap_id=ZmE0YmY2MDEwM2UxNGJlYmJlZTBjNTFiMmU2MjMzNTg=|1507465204|45baa72175776908f370baf137eec5409c0e33cc;z_c0=Mi4xaXhNYUFBQUFBQUFBQU1LRXlHUTlEQmNBQUFCaEFsVk5CcVVCV2dCZjhSQTl1eXVNeXhkSkFhVS1lY0pNbWF4N0xB|1507465222|afa4ac8524f2eb89f8891063409092ef337bb007;infinity_uid=2|1:0|10:1507869842|12:infinity_uid|\
        24:NzIzNTg1NjAzMTIzMzE4Nzg0|6240fce07a5ed083a57c0a00cc5d1d09ad7c6b34b888b9a078893a465afb8ea6;aliyungf_tc=AQAAAPr02Ul3PgsAuEUgd1S7fsxbIIm2;s-q=Howard;si=16id=p3reptm;__utma=51854390.1269669074.1507909546.1507988460.1507990458.3;__utmc=51854390;__utmz=51854390.1507990458.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/gong-chang-shao/activities;__utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1;\
         _xsrf=7f5b0f97-d122-4592-86d7-250a73688a63",
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
