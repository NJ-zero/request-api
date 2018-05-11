# coding=utf-8
# author='Shichao-Dong'
# create time: 2018/5/11 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from jsonpath import jsonpath
import re,json

def get_rcontent(content,jsonpath):
    '''
    从content中读取值，供下一个接口调用
    :param content: 返回的content,为str类型
    :param jsonpath: 从getexceldata中get_jsonpath获取
    :return:
    '''
    value = jsonpath(content,jsonpath)
    return value[0]

def repalce_formdata(data,newdata):
    '''
    替换formdata，将newdata替换，formdata中'change{change}'
    :param data: getexceldata获取的formdata
    :param newdata: 列表中最后一个值
    :return:
    '''
    for k in data.keys():
        pattern = re.search(r"^change{change}", str(data[k]))
        if pattern != None:
            data[k] = newdata
    return data


#测试代码
# dict2 = {
#     'id':111111,
#     'name':'wade',
#     'age':'change{change}'
# }
#
# a=repalce_formdata(dict2,5)
# print type(a),a