# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/12 21:44
file  :login_page.py
===============================
"""
from locator.login_locator import LoginLocator as login_loc
from common.handle_config import conf
from common.basepage import BasePage


class LoginPage(BasePage):
    '''登录页面'''
    # 登录url
    url = conf.get('env', 'service') + conf.get('env', 'login_url')

    def __init__(self, driver):
        super().__init__(driver)
        # 打开登录页面
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    def login(self, user, pwd):
        '''输入账号密码等级登录'''
        # 定位账号输入框
        self.input_text(login_loc.mobile_ele_xpath, user, '输入账号')
        # 定位密码输入框
        self.input_text(login_loc.pwd_ele_xpath, pwd, '输入账号')
        # 点击登录
        self.click_element(login_loc.login_btn_xpath, '点击登录按钮')

    def get_error_info(self):
        '''获取错误信息'''
        return self.wait_element_visibility(login_loc.error_info_xpath, '登录-异常登录窗口错误信息').text

    def get_alert_error_info(self):
        '''获取页面弹窗的错误提示信息'''
        return self.wait_element_visibility(login_loc.alert_error_info_xpath, '登录-异常登录弹窗错误信息').text

    def page_refresh(self):
        '''刷新页面'''
        self.driver.refresh()
