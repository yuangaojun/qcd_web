# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/19 20:25
file  :login_locator.py
===============================
"""
from selenium.webdriver.common.by import By

class LoginLocator():
    '''登录页面的元素定位'''
    # 账号输入框
    mobile_ele_xpath = (By.XPATH, '//*[@name="phone"]')
    # 密码输入框
    pwd_ele_xpath = (By.XPATH, '//*[@name="password"]')
    # 登录按钮
    login_btn_xpath = (By.XPATH, '//*[@class="btn btn-special"]')
    # 失败的提示内容
    error_info_xpath = (By.XPATH, '//*[@class="form-error-info"]')
    # 失败的弹窗
    alert_error_info_xpath = (By.XPATH, '//div[@class="layui-layer-content"]')