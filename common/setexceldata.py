#coding=utf-8
#author='Shichao-Dong'

import xlrd,json,xlwt
from xlutils.copy import copy
import requests
import os

file = r'E:\Request-Excel\testdata\test_data.xls'

def set_data():
    oldWb=xlrd.open_workbook(file,formatting_info=True)
    newWb = copy(oldWb)
    return newWb

def set_statuscode(sheetnum,rows,statuscode):
    newWb=set_data()
    newWs = newWb.get_sheet(sheetnum)
    newWs.write(rows,11,statuscode)
    newWb.save(file)

def set_content(sheetnum,rows,content):
    newWb=set_data()
    newWs = newWb.get_sheet(sheetnum)
    if len(content)>10000:
        newWs.write(rows,12,content[:10000])
    else:
         newWs.write(rows,12,content)
    newWb.save(file)

def set_result(sheetnum,rows,content):
    '''
    写测试结果pass 还是fail
    :param sheetnum: sheet index
    :param rows: 行
    :param content: pass or fail
    :return:
    '''
    newWb=set_data()
    newWs = newWb.get_sheet(sheetnum)

    stylered = xlwt.easyxf('pattern: pattern solid, fore_color red;')
    stylegreen = xlwt.easyxf('pattern: pattern solid, fore_color green;')
    styleyellow = xlwt.easyxf('pattern: pattern solid, fore_color yellow;')

    if content == 'pass':
        newWs.write(rows,13,content,stylegreen)
        newWb.save(file)
    elif content == 'fail':
        newWs.write(rows,13,content,stylered)
        newWb.save(file)
    elif content == 'not execute':
        newWs.write(rows,13,content,styleyellow)
        newWb.save(file)

def set_sql(sheetnum,rows,sqlresult):
        newWb=set_data()
        newWs = newWb.get_sheet(sheetnum)
        newWs.write(rows,14,sqlresult)
        newWb.save(file)