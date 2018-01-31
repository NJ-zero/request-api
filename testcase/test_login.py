#coding=utf-8
#author='Shichao-Dong'

from common import getexceldata as get
from common import setexceldata as set
from common.logs import log
from common import readConfig as conf
from common import connect_DB as db
from common import check_DB as checkdb
from common import check_all as checkall
import unittest
import requests,time,re
import json


# def check():
#     #判断结果是pass还是fail
#     if int(r.status_code) == 200 :
#         if checkdb.check('login',1) == 'pass':
#             print re.search(str(get.get_data('login',1,10)),r.content)
#             if re.search(str(get.get_data('login',1,10)),r.content) != None:
#                 set.set_result(0,1,'pass')
#             else:
#                 set.set_result(0,1,'fail')
#         else:
#             set.set_result(0,1,'fail')
#     else:
#         set.set_result(0,1,'fail')


def login():
    common_url=conf.ReadConfig().getloginConfigValue('url')
    login_url=get.get_data('login',1,2)
    url = common_url + login_url
    data = json.loads(get.get_data('login',1,6))
    header = get.get_data('login',1,7)
    global r
    print url
    # 判断是否执行
    if int(get.get_data('login',1,4))== 1:
        if get.get_data('login',1,3) == 'post':
            r=requests.post(url=url,data=data,headers=header)
            if checkall.checkall('login',1,r.status_code,r.content) == 'pass':
                set.set_result(0,1,'pass')
            elif checkall.checkall('login',1,r.status_code,r.content) == 'fail':
                set.set_result(0,1,'fail')

        elif get.get_data('login',1,3) == 'get':
            r=requests.get(url=url,data=data,headers=header)

            if checkall.checkall('login',1,r.status_code,r.content) == 'pass':
                set.set_result(0,1,'pass')
            elif checkall.checkall('login',1,r.status_code,r.content) == 'fail':
                set.set_result(0,1,'fail')

    elif int(get.get_data('login',1,4))== 0:
        print 'not execute'
        set.set_result(0,1,'not execute')


    #写status_code和content
    set.set_statuscode(0,1,r.status_code)
    set.set_content(0,1,r.content)

    cookie ="WQSESSIONID="+"".join(r.cookies["WQSESSIONID"])
    print cookie
    return cookie

login()
