import requests
import time
import csv
from bs4 import BeautifulSoup

USERNAME = 'gong-chang-shao'
filename = '%s.csv' % (USERNAME)
offset = 0

headers = {
        'Cookie': 'q_c1=28ada5f3722f4c5d93126dc90d73ba06|1492403582000|1492403582000; d_c0="AHDCqImfnguPTrVW0nJimSjiexf7jOf1yxg=|1492403583"; _zap=a66a75d3-06c5-4cae-a4d3-8b33ef75e9af; _xsrf=cd9131c0f32b50a1973f678628692c90; capsion_ticket="2|1:0|10:1492697361|14:capsion_ticket|44:NzdlNGM0Yjc1ZDA1NGZlYmEwMWU0ZmJkYjkwNWMxZjM=|49d838c11200d10de6d24bf67f9d67f21d9b103d32f4bda83c5472defbe5fe43"; r_cap_id="OTVmYTE2YjRhZGRlNGMzMzljZjVkODRiYWMxZTkyMGI=|1492697363|a2a80e98c76ff347e485397c438fd1c0d3035bfb"; cap_id="NjkwNTg1MTFkYjA3NGU4OWFkZGRhMDEwZWNjMWQ0MDc=|1492697363|3fcb0ff569f45a55b116ae6cf7e6babec26b4fca"; l_cap_id="OTc3MGZiNzdlZTY4NDQ1MDg3ODY0ZTQwNjQyNTRkODY=|1492697363|9b11300357019f8cf140870acefad160f65c07c7"; aliyungf_tc=AQAAANh9nT3OrwYAxkUgd/n5mB3Yi3/p; acw_tc=AQAAADhMO1UHNwkAxkUgdxuijGgi8jty; __utma=51854390.1375139231.1492952772.1493364117.1493374940.27; __utmb=51854390.0.10.1493374940; __utmc=51854390; __utmz=51854390.1493358415.25.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/Evans23/answers; __utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1; z_c0=Mi4wQUFEQTBzY2VBQUFBY01Lb2laLWVDeGNBQUFCaEFsVk5HMDRnV1FEaUg0WVpjTWxhczdvWHVCUzhEc2V0a2RfZmxR|1493374998|f64f34d09ace7e7a04ab12ac40d23076dbfd5bc0',
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