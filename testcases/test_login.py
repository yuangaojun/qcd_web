# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/12 20:40
file  :test_login.py
===============================
'''
username:18684720553
password:python
'''
"""
import pytest
from data.case_data import LoginCase
from selenium import webdriver
from page.login_page import LoginPage
from page.index_page import IndexPage
from common.handle_logging import log


@pytest.fixture(scope='class')
def login_fixture():
    # opt = webdriver.ChromeOptions()
    # opt.add_argument('--headless')
    # driver = webdriver.Chrome(options=opt)
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    driver.quit()


class TestLogin():
    '''测试登录'''

    @pytest.mark.parametrize('case', LoginCase.error_case_data)
    def test_except_case(self, case, login_fixture):
        '''登录异常'''
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.page_refresh()
        # 执行登录操作
        login_page.login(case['mobile'], case['pwd'])
        expected = login_page.get_error_info()
        try:
            assert case['expected'] == expected
            log.info('用例执行通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')

    @pytest.mark.parametrize('case', LoginCase.error_alert_data)
    def test_login_alert(self, case, login_fixture):
        '''异常用例，错误信息弹窗提示'''
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.page_refresh()
        login_page.login(case['mobile'], case['pwd'])
        result = login_page.get_alert_error_info()
        expected = case['expected']
        try:
            assert result == expected
            log.info('用例断言通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')

    @pytest.mark.maoyan
    @pytest.mark.parametrize('case', LoginCase.success_case_data)
    def test_login_pass(self, case, login_fixture):
        '''正常登录'''
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.page_refresh()
        login_page.login(case['mobile'], case['pwd'])
        res = index_page.get_user_info()
        try:
            assert '登录成功' == res
            log.info('用例执行通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')
