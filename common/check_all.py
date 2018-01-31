#coding=utf-8
#author='Shichao-Dong'


from common import getexceldata as get
from common import check_DB as checkdb
import re


def checkall(sheetname,i,code,content):
    '''
    检查结果1.status_code 2.db校验 3.content正则匹配
    :param self:
    :param i:  行
    :param code:
    :param content:
    :return:
    '''
    #判断结果是pass还是fail
    if int(code) == 200 :
        if checkdb.check(sheetname,i)[0] == 'pass':
            print re.search(str(get.get_data(sheetname,i,10)),content)!=None
            if re.search(str(get.get_data(sheetname,i,10)),content)!=None:
                return 'pass'
            elif re.search(get.get_data(sheetname,i,10),content) is None:
                return 'fail'
        else:
            return 'fail'
    else:
        return 'fail'


