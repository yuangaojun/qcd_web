# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/21 20:08
file  :test_invest.py
===============================
"""

'''
投资功能的实现：
前置条件：
1.打开浏览器，访问登录页面
2.需要登录：（账户要有钱，需要有投资的项目）
3.选定项目，点击抢投标

执行用例
操作步骤
1.输入投资的金额
2.点击投资（如果输入的不是10的整数倍，点击时没有任何效果的）
校验结果：
情况一：输入的金额不是10的整数倍，点击按钮是会出现对应的额提示：校验点击按钮上的提示信息是否和预期一致
情况二：输入的数据不符合要求（0，负数，超出最大可投金额），弹框提示对应的错误：校验弹框的提示信息是否和预期一致
情况三：投资成功，成功的弹框提示:
1.校验是否弹出投资成功。
2.校验投资之前和投资之后的余额变化的值是否和投资金额一致
    投资之前要去获取账号余额（可以在输入框标签中获取）
    投资之后再去获取账号余额（点击成功信息查看按钮，会进入用户页面，获取投资之后的余额）
    相减，
    
后置条件：
关闭浏览器

# 分析投资用例执行的过程：涉及到了那些页面的操作？
1.登录页面--->>输账号，密码点击登录
2.首页--->>选中项目，点击抢投标（待封装）--ok
3.投资的项目页面：
    -获取账户可用余额（待封装）ok
    -输入投资金额（待封装）ok
    -点击投资（待封装）
    -投资成功-获取投标成功的信息（待封装）
    -投资成功-点击查看并激活（待封装）
    
    -投资失败-获取按钮的提示信息（待封装）
    -投资失败-获取弹框的错误信息（待封装）
        
4.用户页面
    -获取可用余额（待封装）

'''
import pytest
import decimal
from selenium import webdriver
from page.login_page import LoginPage
from page.index_page import IndexPage
from page.invest_page import InvestPage
from page.unserinfo_page import UserInfo
from common.handle_config import conf
from data.case_data import InvestCase
from common.handle_logging import log
from locator.index_locator import IndexLocator as index_loc


@pytest.fixture(scope='class')
def invest_fixture():
    # opt = webdriver.ChromeOptions()
    # opt.add_argument('--headless')
    # driver = webdriver.Chrome(options=opt)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    login_page = LoginPage(driver)
    # 登录首页
    login_page.login(conf.get('test_data', 'username'), conf.get('test_data', 'password'))
    index_page = IndexPage(driver)
    # 首页点击抢投标
    index_page.click_element(index_loc.bid_btn_ele, '点击抢投标')
    invest_page = InvestPage(driver)
    # 滚动窗口到投资金额输入框
    invest_page.window_move_amount_inout()
    user_page = UserInfo(driver)
    yield invest_page, user_page
    driver.quit()


class TestInvest():


    @pytest.mark.parametrize('case', InvestCase.error_case_data)
    def test_invest_error_btn(self, case, invest_fixture):
        '''投资失败-页面按钮上出现提示的用例'''
        invest_page, user_page = invest_fixture
        # 清空投资金额输入框
        invest_page.clear_invest_input()
        # 输入投资金额
        invest_page.input_invest_money(case['amount'])
        # 获取投标按钮上的信息
        res = invest_page.get_invest_btn_error()
        try:
            assert case['expected'] == res
            log.info('用例执行通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')

    @pytest.mark.parametrize('case', InvestCase.error_alert_data)
    def test_invest_error_window(self, case, invest_fixture):
        '''投资失败-页面按钮上出现提示的用例'''
        invest_page, user_page = invest_fixture
        # 清空投资金额输入框
        invest_page.clear_invest_input()
        # 输入投资金额
        invest_page.input_invest_money(case['amount'])
        # 点击投标
        invest_page.click_invest()
        # 获取投标失败时弹窗提示的信息
        res = invest_page.get_window_error()
        # 点击错误提示框确认按钮关闭提示框
        invest_page.click_errorinfo_quren()
        try:
            assert case['expected'] == res
            log.info('用例执行通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')

    @pytest.mark.parametrize('case', InvestCase.success_case_data)
    def test_invest_success(self, case, invest_fixture):
        '''投资失败-页面按钮上出现提示的用例'''
        invest_page, user_page = invest_fixture
        # 刷新页面
        invest_page.page_refresh()
        # 获取投标之前的用户余额
        current_amount = invest_page.get_user_amount()
        # 输入投资金额
        invest_page.input_invest_money(case['amount'])
        # 点击投标
        invest_page.click_invest()
        # 获取投标成功时弹窗提示的信息
        res = invest_page.get_invest_success_info()
        # 点击查看并激活
        invest_page.click_view_activation()
        # 获取用户投标后的余额
        user_amount = user_page.get_user_money_amount()
        # 投资前的余额减去投资后的余额
        invest_money = decimal.Decimal(current_amount) - decimal.Decimal(user_amount)
        try:
            assert case['expected'] == res and invest_money == case['amount']
            print('res:{}'.format(res))
            log.info('用例执行通过')
        except AssertionError as e:
            log.error('用例断言失败')
            log.exception(e)
            raise e
        else:
            log.info('用例执行完毕')


if __name__ == '__main__':
    pytest.main()
