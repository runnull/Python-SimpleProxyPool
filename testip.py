# +----------------------------------------------------------------------
# | Python-SimpleProxyPool
# +----------------------------------------------------------------------
# | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
# +----------------------------------------------------------------------
# | Author: 青衫依旧
# +----------------------------------------------------------------------

import requests
import time
import threading
import mysql

url = 'http://www.baidu.com/' 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
lock = threading.Lock() #使用线程锁


#利用多线程，验证IP
def verify_ip(data):
    #http://icanhazip.com/
    print(data)
    ip = data[0]
    ida = data[1]

    try:
        # 先要获取锁:
        lock.acquire()
        #解开锁
        lock.release()

        proxies = {'http': ip}

        r = requests.get(url, headers=headers, proxies=proxies,timeout=15)
        # 如果requests成功，表示验证成功，打印出IP
        # print(r.text)
        if(r.status_code == 200):
            mysql.UPDATE_IP(ida,'0')
            print('Success:'+data[0])
        else:
            mysql.UPDATE_IP(ida,'1')
            print('Failure:'+data[0])

    except:
        mysql.UPDATE_IP(ida,'1')
        print('Error')


def test(ip_list):
    for ip in ip_list:
        data = [ip[0],ip[1]]
        threading.Thread(target=verify_ip,args=(data,)).start()
        # t.setDaemon(True)
        time.sleep(1)

def test_ip():
    db = mysql.pymysql.connect(mysql.host,mysql.user,mysql.password,mysql.dbname)
    cursor = db.cursor()
    idb = '0'
    var = 1
    while var == 1:
        ip_list = []
        sql = "SELECT * FROM ip WHERE `ok` = '-1' and `id` >= '%s'" % idb
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ida = row[0]
            ip = row[1]
            port = row[2]
            ip_list.append([ip+':'+str(port),str(ida)])
            idb = ida

        threading.Thread(target=test,args=(ip_list,)).start()

        time.sleep(10)
    
        

