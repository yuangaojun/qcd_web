# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/21 22:59
file  :unserinfo_page.py
===============================
"""

from common.basepage import BasePage
from locator.user_info_locator import UserInfo as user_loc


class UserInfo(BasePage):
    '''用户信息页面操作'''

    def get_user_money_amount(self):
        '''获取用户投资成功后的余额'''
        amount = self.get_element_text(user_loc.amount_ele, '用户页面-获取用户余额')
        return amount.replace('元', '')
