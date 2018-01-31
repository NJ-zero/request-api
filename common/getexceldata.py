#coding=utf-8
#author='Shichao-Dong'

import xlrd,json,xlwt
import requests
import os

file = r'E:\Request-Excel\testdata\test_data.xls'

def get_data(name,rows,cols):
    '''
    读取表格数据
    :param name:sheet名称
    :param rows: 行
    :param cols: 列
    :return:
    '''
    alldata=xlrd.open_workbook(file)
    sheet = alldata.sheet_by_name(name)

    value = sheet.cell(rows,cols).value
    return value

def get_formdata(name,rows):
    '''
    读取请求参数
    :param name: sheet名称
    :param rows: 行
    :return:
    '''
    alldata=xlrd.open_workbook(file)
    sheet = alldata.sheet_by_name(name)

    value = sheet.cell(rows,6).value
    if value == '':
        return value
    else:
        return json.loads(value)


def get_nrows(name):
    '''
    读取行数
    :param name: sheet名称
    :return:
    '''
    alldata=xlrd.open_workbook(file)
    sheet = alldata.sheet_by_name(name)
    nrows = sheet.nrows
    return nrows

