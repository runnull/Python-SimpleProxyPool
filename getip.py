# +----------------------------------------------------------------------
# | Python-SimpleProxyPool
# +----------------------------------------------------------------------
# | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
# +----------------------------------------------------------------------
# | Author: 青衫依旧
# +----------------------------------------------------------------------


import requests
import lxml
from bs4 import BeautifulSoup
import mysql

def get_html(url,flag=True):
    try:
        headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'        }
        res = requests.get(url,headers=headers)
        res.raise_for_status()
        if(flag):
            res.encoding = 'utf-8'
        else:
            res.encoding = 'gb2312'
        
        return res.text
    except:
        print('请求异常')

def get_66ip():
    for index in range(1,101):
        res = get_html('http://www.66ip.cn/{}.html'.format(index),flag=False)
        soup = BeautifulSoup(res,'lxml')
        tr_list = soup.find_all(name='tr')
        for temp in tr_list[2:]:
            td_list = temp.find_all(name='td')
            ip = "".join(td_list[0].string.split())
            port = "".join(td_list[1].string.split())
            #ip_list.append(td_list[0].string+':'+td_list[1].string)
            mysql.INSERT_IP(ip,port,'66ip')
    mysql.time.sleep(10)

def get_kxip():
    for index in range(1,101):
        res = get_html('http://www.kxdaili.com/dailiip/1/{}.html'.format(index))
        soup = BeautifulSoup(res,'lxml')
        tr_list = soup.find_all(name='tr')
        for temp in tr_list[2:]:
            td_list = temp.find_all(name='td')
            ip = "".join(td_list[0].string.split())
            port = "".join(td_list[1].string.split())
            #ip_list.append(td_list[0].string+':'+td_list[1].string)
            mysql.INSERT_IP(ip,port,'kxip')

    mysql.time.sleep(10)

def get_kdip():
    for index in range(1,101):
        res = get_html('https://www.kuaidaili.com/free/inha/{}/'.format(index))
        soup = BeautifulSoup(res,'lxml')
        tr_list = soup.find_all(name='tr')
        for temp in tr_list[2:]:
            td_list = temp.find_all(name='td')
            ip = "".join(td_list[0].string.split())
            port = "".join(td_list[1].string.split())
            #ip_list.append(td_list[0].string+':'+td_list[1].string)
            mysql.INSERT_IP(ip,port,'kdip')

    mysql.time.sleep(10)

def get_89ip():
    for index in range(1,79):
        res = get_html('http://www.89ip.cn/index_{}.html'.format(index))
        soup = BeautifulSoup(res,'lxml')
        tr_list = soup.find_all(name='tr')
        for temp in tr_list[1:]:
            td_list = temp.find_all(name='td')
            #ip_list.append(td_list[0].string+':'+td_list[1].string)
            ip = "".join(td_list[0].string.split())
            port = "".join(td_list[1].string.split())
            mysql.INSERT_IP(ip,port,'89ip')

    mysql.time.sleep(10)