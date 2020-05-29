# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/21 20:52
file  :invest_page.py
===============================
"""
from locator.invest_locator import InvestLocator as loc
from common.basepage import BasePage


class InvestPage(BasePage):

    def get_user_amount(self):
        '''获取用户投资前的余额'''
        return self.get_element_attribute(loc.invest_amount_input, 'data-amount', '投资-获取用户投资前的余额')

    def input_invest_money(self, money):
        '''输入投资金额'''
        return self.input_text(loc.invest_amount_input, money, '投资-输入投资金额')

    def click_invest(self):
        '''点击投资'''
        return self.click_element(loc.invest_btn, '投资-点击投资按钮')

    def get_window_error(self):
        '''获取投资失败-弹框错误提示信息'''
        return self.get_element_text(loc.window_error, '投资-弹框错误提示信息')

    def get_invest_btn_error(self):
        '''获取投标按钮提示错误信息'''
        return self.get_element_text(loc.invest_btn, '投资-投标按钮提示错误信息')

    def click_errorinfo_quren(self):
        '''点击投标金额错误提示确认-关闭弹窗'''
        return self.click_element(loc.window_queren, '投资-点击错误提示弹窗确认按钮')

    def get_invest_success_info(self):
        '''投标成功-弹窗提示信息'''
        return self.get_element_text(loc.invest_success, '投资成功-投资成功提示信息')

    def click_view_activation(self):
        '''投资成功-点击查看并激活'''
        return self.click_element(loc.view_activation, '投资成功-点击查看并激活')

    def clear_invest_input(self):
        '''清空投资金额输入框'''
        return self.clear_input(loc.invest_amount_input, '投资-清空投资金额输入框')

    def window_move_amount_inout(self):
        '''滚动窗口到投资金额输入框'''
        return self.window_move_element(loc.invest_amount_input, '滚动窗口到投资金额输入框')
