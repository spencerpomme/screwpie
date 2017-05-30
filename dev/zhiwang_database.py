import requests
import time
import csv
from bs4 import BeautifulSoup
from progressbar import ProgressBar

TOTAL_PAGE = 41180

filename = 'patent.csv'
file = open(r'%s' % filename, 'w', newline='', encoding='utf8')
writer = csv.writer(file)

headers = {
        'Cookie': 'Ecp_ClientId=4170421000200002642; cnkiUserKey=d21512b7-3120-e0ca-f011-4248e51c71a2; ASP.NET_SessionId=24c34155q5ky5uz1ryiaf545; AutoIpLogin=; LID=; Ecp_IpLoginFail=170510119.32.69.150; SID=130102; CurTop10KeyWord=%2c%u5e7f%u4e1c; FileNameM=cnki%3A',
        'Host':'dbpub.cnki.net',
        'Referer':'http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?curpage=4&RecordsPerPage=50&QueryID=0&ID=SCPD&turnpage=1&systemno=&NaviDatabaseName=SCPD_ZJCLS&NaviField=%e4%b8%93%e9%a2%98%e5%ad%90%e6%a0%8f%e7%9b%ae%e4%bb%a3%e7%a0%81&navigatorValue=&subBase=all',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Connection': 'keep-alive'
    }
bar = ProgressBar(max_value=TOTAL_PAGE, redirect_stdout=True)
for i in range(1,TOTAL_PAGE + 1):
    test_url = 'http://dbpub.cnki.net/Grid2008/Dbpub/Brief.aspx?curpage='+('%d' % i)+'&RecordsPerPage=50&QueryID=371&ID=SCPD&turnpage=1&systemno=&NaviDatabaseName=SCPD_ZJCLS&NaviField=%E4%B8%93%E9%A2%98%E5%AD%90%E6%A0%8F%E7%9B%AE%E4%BB%A3%E7%A0%81&navigatorValue=&subBase=all'
    res = requests.get(test_url, headers=headers)
    print('Acquiring page %d...' % i)

    soup = BeautifulSoup(res.text, 'lxml')
    table = soup.findAll('table', {'class': 's_table'})
    try:
        rows = table[0].findAll('tr')
    except:
        print('Page %d failed, retrying...' % i)
        i -= 1
        time.sleep(0.5)
        continue
    for row in rows[1:]:
        cols = row.findAll('td',{'class':'s_tabletd_rb'})
        # print(cols[0].text, cols[1].text, cols[2].text, cols[3].text, cols[4].text, cols[5].text)
        writer.writerow([cols[1].a.string,
                         cols[1].a.attrs['href'],
                         cols[2].string.lstrip(),
                         cols[3].string.lstrip(),
                         cols[4].string.lstrip(),
                         cols[5].string.lstrip()]
                         )
    bar.update(i)
    time.sleep(1)