# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/19 20:26
file  :index_locator.py
===============================
"""
from selenium.webdriver.common.by import By


class IndexLocator():
    # 用户信息
    user_info_xpath = (By.XPATH, '//*[contains(text(),"我的帐户")]')
    # 退出
    quit_xpath = (By.XPATH, '//a[text()="退出"]')
    # 项目抢投标的节点
    bid_btn_ele = (By.XPATH,'(//a[text()="抢投标"])[1]')#(//*[@class="graph"]//*[@class="btn btn-special"])[1]
