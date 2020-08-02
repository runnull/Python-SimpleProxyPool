# +----------------------------------------------------------------------
# | Python-SimpleProxyPool
# +----------------------------------------------------------------------
# | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
# +----------------------------------------------------------------------
# | Author: 青衫依旧
# +----------------------------------------------------------------------


import getip
import testip
import threading
import time

def run():
    print('开启获取ip线程')
    threading.Thread(target=getip.get_66ip).start()
    threading.Thread(target=getip.get_kxip).start()
    threading.Thread(target=getip.get_kdip).start()
    threading.Thread(target=getip.get_89ip).start()
    # getip.get_66ip()
    # getip.get_kxip()
    # getip.get_kdip()
    # getip.get_89ip()

def test():
    print('开启验证ip线程')
    testip.test_ip()

threading.Thread(target=run).start()
time.sleep(5)
threading.Thread(target=test).start()


