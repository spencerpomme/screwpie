import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/people/gong-chang-shao/followers?page=1'
headers_1 = {
        'Cookie': 'q_c1=02d871bad1b6434086fe737982df2a3d|1484706667000|1484706667000; d_c0="ABACeiPuKwuPTi544NVJjPTaS40_R6gz5LI=|1484706668"; _zap=a062f552-499f-4c8f-a261-09689401a4bd; r_cap_id="MTI1NDhiMTlhNjdiNGY4MmExNGI2MzllYzY2MWQ4MWY=|1484706669|9b85317ef6428eb036896fab0c5d1ea063188a67"; _xsrf=1e33b2b87456dd182f2af4eefb3fad40; capsion_ticket="2|1:0|10:1485433540|14:capsion_ticket|44:Y2VlZWZlNjZjMzY4NDczMjk2ZDA1YmEzMTY0YzhkNjU=|0bb0ef50e556525a36d01dc95482e48522759e46edb6659d7d94b9fbce220d3b"; l_cap_id="NzYzMGU2MjliMDkxNGJiNGExNDM2ZTQxY2E2ZDc1YzY=|1486092324|567b3feb44c5dcf865a306aaa42a00013f34ddb1"; cap_id="ZGJjMzQ3N2MzNzdiNDM4YmFkYTBlNDAyM2Y1YjZjMDg=|1486092324|7903a0737657c97c25e6086091e6b74dfa1e9a4f"; login="ZDA3ODZmM2YxNGFjNDJhNmJlM2Y5MmQ4OGU5NmVkMGQ=|1486092328|389cf8961075eaf257d9e121d30ee56b3c3fa737"; aliyungf_tc=AQAAAJbPnl9/fggARkUgd+pTOHvDmxp3; z_c0=Mi4wQUFEQTBzY2VBQUFBRUFKNkktNHJDeGNBQUFCaEFsVk5YWVc3V0FBeTRjYWNjamktZE1EbERmWnVqQ1NqN1FVREpR|1486097058|a450571744a3b36cc4a662636be40723591ce3fc; __utma=51854390.31450228.1486043719.1486083823.1486086724.3; __utmb=51854390.110.9.1486096677777; __utmc=51854390; __utmz=51854390.1486086724.3.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1',
        'Host':'www.zhihu.com',
        'Referer':'http://www.zhihu.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding':'gzip',
        'Connection': 'keep-alive'
    }

headers_2 = {
        'Cookie': 'q_c1=02d871bad1b6434086fe737982df2a3d|1484706667000|1484706667000; d_c0="ABACeiPuKwuPTi544NVJjPTaS40_R6gz5LI=|1484706668"; _zap=a062f552-499f-4c8f-a261-09689401a4bd; r_cap_id="MTI1NDhiMTlhNjdiNGY4MmExNGI2MzllYzY2MWQ4MWY=|1484706669|9b85317ef6428eb036896fab0c5d1ea063188a67"; _xsrf=1e33b2b87456dd182f2af4eefb3fad40; capsion_ticket="2|1:0|10:1485433540|14:capsion_ticket|44:Y2VlZWZlNjZjMzY4NDczMjk2ZDA1YmEzMTY0YzhkNjU=|0bb0ef50e556525a36d01dc95482e48522759e46edb6659d7d94b9fbce220d3b"; l_cap_id="NzYzMGU2MjliMDkxNGJiNGExNDM2ZTQxY2E2ZDc1YzY=|1486092324|567b3feb44c5dcf865a306aaa42a00013f34ddb1"; cap_id="ZGJjMzQ3N2MzNzdiNDM4YmFkYTBlNDAyM2Y1YjZjMDg=|1486092324|7903a0737657c97c25e6086091e6b74dfa1e9a4f"; login="ZDA3ODZmM2YxNGFjNDJhNmJlM2Y5MmQ4OGU5NmVkMGQ=|1486092328|389cf8961075eaf257d9e121d30ee56b3c3fa737"; aliyungf_tc=AQAAAJbPnl9/fggARkUgd+pTOHvDmxp3; __utma=51854390.1155275139.1486104420.1486104420.1486104420.1; __utmc=51854390; __utmz=51854390.1486104420.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/gong-chang-shao/activities; __utmv=51854390.100-1|2=registration_date=20131007=1^3=entry_date=20131007=1; z_c0=Mi4wQUFEQTBzY2VBQUFBRUFKNkktNHJDeGNBQUFCaEFsVk5YWVc3V0FBeTRjYWNjamktZE1EbERmWnVqQ1NqN1FVREpR|1486104542|a944a19d1f5a116996120e82168331fed3005bb3',
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




g = ('https://www.zhihu.com/api/v4/members/gong-chang-shao/followers'
     '?include=data%5B*%5D.answer_count%2Carticles_count%2Cfollower_count'
     '%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)'
     '%5D.topics'
     '&offset=0'
     '&limit=20')
get = requests.get(g, headers=headers_1)

total_follower = get.json()['paging']['totals']
offset = 2550
while offset < total_follower:
    url = ('https://www.zhihu.com/api/v4/members/gong-chang-shao/followers'
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







    
    
