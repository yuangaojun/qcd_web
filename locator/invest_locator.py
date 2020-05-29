# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/21 20:47
file  :invest_locator.py
===============================
"""
from selenium.webdriver.common.by import By


class InvestLocator():
    '''投资页面的元素定位'''

    # 投资金额输入框xpath
    invest_amount_input = (By.XPATH, '//*[@class="form-control invest-unit-investinput"]')
    # 投标点击按钮
    invest_btn = (By.XPATH, '//button[@class="btn btn-special height_style"]')
    # 投资成功-投资成功提示信息
    invest_success = (By.XPATH, '//div[@class="capital_font1 note" and text()="投标成功！"]')
    # 投资成功-查看并激活
    view_activation = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败-弹框提示
    window_error = (By.XPATH, '//*[@class="text-center"]')
    # 投资失败-弹框关闭确认按钮
    window_queren = (By.XPATH, '//a[@class="layui-layer-btn0"]')

