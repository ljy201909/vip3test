# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.26

import unittest
from ddt import ddt,data,unpack
import readExcel
import json
import requests

#调用readExcel()函数，将所有sheet存储在L中
L = readExcel.readExcel()
#调用returnSheet()函数，创建sheet1和sheet2
L1 = readExcel.returnSheet(L[0])
print(L1)
L2 = readExcel.returnSheet(L[1])
print(L2)
#将sheet2中的数据由str转换成json，方便后面调用
for i in range(1,len(L2)):
    L2[i][1] = json.loads(L2[i][1])
#
# #将结果存入新的Excel
# writeResult(1,result)

@ddt
class MyTestCase1(unittest.TestCase):
    @data({'urlstr':L1[1][1],'payload':L2[1][1]})
    @unpack
    def test01(self,urlstr,payload):
        r = requests.post(url=urlstr, data=payload)
        if r.json()['data']['username'] == payload['username']:
            result = 'success'
            readExcel.writeResult(1,result)
        else:
            result = 'failed'
            readExcel.writeResult(1,result)

    @data({'urlstr':L1[2][1],'payload':L2[2][1]})
    @unpack
    def test02(self, urlstr, payload):
        r = requests.post(url=urlstr, data=payload)
        if r.json()['errorMsg'] == None:
            result = 'success'
            readExcel.writeResult(2,result)
        else:
            result = r.json()['errorMsg']
            readExcel.writeResult(2,result)

    # @data(L1[3][1], L2[3][1])
    # @unpack
    # def test03(self, urlstr, payload):
    #     r = requests.post(url=urlstr, data=payload)
    #     if r.json()['data']['username'] == payload['username']:
    #         result = 'success'
    #         readExcel.writeResult(3,result)
    #     else:
    #         result = 'failed'
    #         readExcel.writeResult(3,result)


if __name__ == '__main__':
    unittest.main()
