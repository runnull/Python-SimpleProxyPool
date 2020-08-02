# +----------------------------------------------------------------------
# | Python-SimpleProxyPool
# +----------------------------------------------------------------------
# | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
# +----------------------------------------------------------------------
# | Author: 青衫依旧
# +----------------------------------------------------------------------


import pymysql
import time

host = 'localhost' # 数据库地址
user = 'root'      # 数据库用户名
password = 'root'  # 数据库密码
dbname = 'test_ip' # 数据库名称

def INSERT_IP(ip,port,come):
    db = pymysql.connect(host,user,password,dbname)
    cursor = db.cursor()
    sql = "INSERT INTO ip(ip,port, ok, time,come) VALUES ('%s','%s',-1,'%s','%s')" % (ip,port,get_time(),come)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    db.close()

def UPDATE_IP(ida,ok):
    db = pymysql.connect(host,user,password,dbname)
    cursor = db.cursor()
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = "UPDATE ip SET `ok` = '%s',`time` = '%s' WHERE ID = '%s'" % (ok,str(times),ida)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    db.close()
    

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())