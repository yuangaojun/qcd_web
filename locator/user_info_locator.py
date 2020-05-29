# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/21 22:39
file  :user_info_locator.py
===============================
"""
from selenium.webdriver.common.by import By


class UserInfo():
    '''用户信息页面元素'''

    # 用户余额
    amount_ele = (By.XPATH, '//*[@class="color_sub"]')
