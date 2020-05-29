# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/14 20:27
file  :case_data.py
===============================
"""


class LoginCase():
    '''登录功能的用例数据'''

    # 正常登录的用例
    success_case_data = [
        {'mobile': '18684720553', 'pwd': 'python', 'expected': '登录成功'}
    ]
    # 异常登录的用例，错误提示在页面上
    error_case_data = [
        {'mobile': '', 'pwd': 'python', 'expected': '请输入手机号'},
        {'mobile': '18684720553', 'pwd': '', 'expected': '请输入密码'},
        {'mobile': '1868472055@', 'pwd': 'python', 'expected': '请输入正确的手机号'}
    ]
    # 异常登录的用例，错误提示在弹窗中
    error_alert_data = [
        {'mobile': '18684720550', 'pwd': 'python112', 'expected': '此账号没有经过授权，请联系管理员!'},
        {'mobile': '18684720553', 'pwd': 'python888', 'expected': '帐号或密码错误!'}
    ]


class InvestCase():
    '''投标功能的用例数据'''

    # 投资成功的用例
    success_case_data = [
        {'amount': '100', 'expected': '投标成功！'}
    ]
    # 投资失败的用例，错误提示在页面上
    error_case_data = [
        {'amount': '1', 'expected': '请输入10的整数倍'},
        {'amount': '0001', 'expected': '请输入10的整数倍'},
        {'amount': '109', 'expected': '请输入10的整数倍'},
        {'amount': '!@##@', 'expected': '请输入10的整数倍'}
    ]
    # 投资失败的用例，错误提示在弹窗中
    error_alert_data = [
        {'amount': ' ', 'expected': '请正确填写投标金额'},
        {'amount': '0', 'expected': '请正确填写投标金额'},
        {'amount': '-100', 'expected': '请正确填写投标金额'},
        {'amount': '2000100', 'expected': '购买标的金额不能大于标总金额'}
    ]
