#coding=utf-8
#author='Shichao-Dong'


import sys,os
reload(sys)
sys.path.append(r'E:\Request-Excel\testcase')
import unittest
import HTMLTestRunner
import time

from testcase.test_cm import Cm


def testsuit():
    suite = unittest.TestSuite()
    suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Cm),



                   ])

    runner = unittest.TextTestRunner(verbosity=2)

    runner.run(suite)

if __name__ =="__main__":
    testsuit()


