# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/17 14:00
file  :conftest.py
===============================
"""
import pytest
from selenium import webdriver
from page.login_page import LoginPage
from page.index_page import IndexPage


@pytest.fixture()
def login_case_fixture():
    '''测试用例前置后置条件'''
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    driver.quit()
