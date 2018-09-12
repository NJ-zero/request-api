#coding=utf-8
#author='Shichao-Dong'

import xlrd,json,xlwt
import requests
import os,re

# file = r'E:\Request-Excel\testdata\test_data.xls'
file = '../testdata/test_data.xls'

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

def get_formdata(name,rows,change):
    '''
    读取请求参数,change为依赖参数，读取自上一个接口返回
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
        value=json.loads(value)
        for k in value.keys():
            pattern = re.search(r"^change{change}", str(value[k]))
            if pattern != None:
                value[k] = change
            elif pattern is None:
                pass
        return value

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

def get_jsonpath(name,rows):
    '''
    读取依赖，供下面参数传值
    :param name: sheet名称
    :param rows: 行
    :return:
    '''
    alldata = xlrd.open_workbook(file)
    sheet = alldata.sheet_by_name(name)

    value = sheet.cell(rows, 15).value
    if value == '' or value is None:
        return ''
    else:
        return str(value)

#  测试
# a = get_jsonpath('cm',1)
# print a,type(a)
# from jsonpath import jsonpath
# dict = {"a":"aaa","class": {"students": [{"student_id": "1", "name": "bob", "sex": "male", "age": 6},
#                                {"student_id": "2", "name": "amy", "sex": "female", "age": 6},
#                                {"student_id": "3", "name": "pery", "sex": "male", "age": 5}],
#                   "teachers": {"teacher_id": "1", "name": "anne", "sex": "female", "age": 32}}}
# name =jsonpath(dict, a)
# print(name)
