#coding=utf-8
#author='Shichao-Dong'

from common import readConfig as conf
from common import connect_DB as db
from common import getexceldata as get
from common import setexceldata as set


def check(name,rows):
    '''
    查询sql检查
    :param name:sheetname
    :param rows: 行
    :return:
    '''
    execute = int(get.get_data(name,rows,7))
    if execute == 0:
        return ('pass','')
    elif execute == 1:
        sql = sql=get.get_data(name,rows,8)

        actual_result = db.DB().select(sql)
        expext_result = get.get_data(name,rows,9)

        if actual_result == expext_result:
            return ('pass',actual_result)
        else:
            return ('fail',actual_result)

