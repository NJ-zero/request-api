#coding=utf-8
#author='Shichao-Dong'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import test_login
from common import getexceldata as get
from common import setexceldata as set
from common.logs import log
from common import readConfig as conf
from common import connect_DB as db
from common import check_DB as checkdb
from common import check_all as checkall
import unittest,json
import requests,time,re


class Cm(unittest.TestCase):

    def test_cm(self):
        cookie = test_login.login()
        common_url=conf.ReadConfig().getloginConfigValue('url')
        jsondatas=['data']
        for i in range(int(get.get_nrows('cm'))-1):
            #将jsonpath存入列表中
            jsondata=get.get_jsonpath('cm',i+1)
            if jsondata !='':
                jsondatas.append(jsondata)
            # 判断是否执行
            if int(get.get_data('cm',i+1,4))== 1:
                login_url=get.get_data('cm',i+1,2)
                url = common_url + login_url
                data = get.get_formdata('cm',i+1,jsondatas[-1])
                header = {"Content-Type": "application/x-www-form-urlencoded","Cookie":cookie}
                global r
                print url
                if get.get_data('cm',i+1,3) == 'post':
                    r=requests.post(url=url,headers=header,data=data)

                    if checkall.checkall('cm',i+1,r.status_code,r.content) == 'pass':
                        set.set_result(2,i+1,'pass')
                    elif checkall.checkall('cm',i+1,r.status_code,r.content) == 'fail':
                        set.set_result(2,i+1,'fail')

                    set.set_statuscode(2,i+1,r.status_code)
                    set.set_content(2,i+1,r.content.decode('UTF-8'))
                    set.set_sql(2,i+1,checkdb.check('cm',i+1)[1])

                elif get.get_data('cm',i+1,3) == 'get':
                    r=requests.get(url=url,headers=header,data=data)

                    if checkall.checkall('cm',i+1,r.status_code,r.content) == 'pass':
                        set.set_result(2,i+1,'pass')
                    elif checkall.checkall('cm',i+1,r.status_code,r.content) == 'fail':
                        set.set_result(2,i+1,'fail')

                    set.set_statuscode(2,i+1,r.status_code)
                    set.set_content(2,i+1,r.content.decode('UTF-8'))
                    set.set_sql(2,i+1,checkdb.check('cm',i+1)[1])

            elif int(get.get_data('cm',i+1,4))== 0:
                print 'not execute'
                set.set_result(2,i+1,'not execute')

if __name__ == "__main__":
    Cm()

