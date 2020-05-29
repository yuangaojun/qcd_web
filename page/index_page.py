# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/12 22:34
file  :index_page.py
===============================
"""
from locator.index_locator import IndexLocator as index_loc
from common.basepage import BasePage


class IndexPage(BasePage):
    '''用户信息页面封装'''

    def get_user_info(self):
        '''获取用户信息'''
        try:
            self.get_element(index_loc.user_info_xpath,'首页-获取我的账户信息')
            return '登录成功'
        except:
            return '登录失败'

    def click_quit(self):
        '''点击退出'''
        self.click_element(index_loc.quit_xpath,'首页-点击退出登录')

    def click_bid(self):
        '''点击抢投标'''
        self.click_element(index_loc.bid_btn_ele,'首页-点击抢投标')
