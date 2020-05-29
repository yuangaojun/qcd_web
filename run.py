# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/12 22:55
file  :run.py
===============================
"""
# from selenium import webdriver

# # 设置driver以无头浏览器模式运行
# opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
# driver = webdriver.Chrome(options=opt)
# # 访问百度
# driver.get('http://www.baidu.com')
# driver.save_screenshot('baidu.png')
# driver.quit()

'''
web自动化的用例，如果放到linux服务器上面能不能执行
#1. 将chrome设置为无头浏览的模式（浏览器在后台执行，执行的过程中不会显示浏览器的页面）
#2.linux安装好web自动化执行的环境（python环境+用到的第三方库都要安装）
#3.在服务器上安装chrome浏览器

# 重复执行用例多次插件:pytest-repeat



'''

# import unittest
# from HTMLTestRunner import HTMLTestRunner
import os
#
import pytest
# #
# #
# def pytest_all():
#     # pytest.main('--html=report/py_report.html')
#     # 运行测试用例-生成allure报告数据
#     pytest.main(['--alluredir=allure_report'])
# #
# #
# # def res_run():
# #     # 失败的用例重复执行：pip install pytest-rerunfailures
# #     pytest.main(['-m mytest', '--reruns', '3', 'reruns-delay', '2'])
# #
# #
# # def pytest_maoyan():
# #     pytest.main('-m maoyan')
# #
# #
# # def run():
# #     suite = unittest.defaultTestLoader.discover(start_dir=r'F:\lemonban\lianxi\qcd_web\testcases',
# #                                                 pattern='test*.py',
# #                                                 top_level_dir=None)
# #     report_file = open('report.html', 'wb')
# #     runner = HTMLTestRunner(title='py27第一份web自动化测试报告', stream=report_file,
# #                             description='web自动化测试报告描述', verbosity=2)
# #     runner.run(suite)
# #
# #
# # 运行服务
# def allure_report():
#     os.system('allure serve allure_report')
# #
# if __name__ == '__main__':
# # #     # run()
# #     pytest_all()
# #     # pytest_maoyan()
#     allure_report()
pytest.main()