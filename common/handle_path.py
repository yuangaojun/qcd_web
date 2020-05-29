# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/4/15 10:07
file  :handle_path.py
===============================
"""
import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 测试报告路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')

# 日志文件路径
LOG_DIR = os.path.join(BASE_DIR,'logs')

# 错误截图的路径
ERROR_IMG = os.path.join(BASE_DIR,'error_image')

