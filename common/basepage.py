# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2020/5/23 10:04
file  :basepage.py
===============================
"""
'''
1.显示等待（元素加载，
            元素可见，
            元素可点击）
2.获取元素文本
3.点击元素
4.获取元素属性
5.文本输入
6.窗口拖动
7.滑动到元素可见
8.执行js代码

# 如果元素定位出错了要不要进行日志输出
    日子输出可以封装到basepage的基础操作中
    
# 如果元素定位出错了，页面截图
    错误截图一起封装
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_logging import log
from common.handle_path import ERROR_IMG
import time
import os


class BasePage():
    '''把页面一些常见的功能操作全部封装到这里'''

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator, img_info, timeout=20, poll_frequency=0.5):
        '''等待元素可见'''
        # 等待元素之前获取当前时间
        start_time = time.time()
        try:
            ele_visibility = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 输出日志
            log.error('元素--{}--等待可见超时'.format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_imge(img_info)
            raise e
        else:
            # 元素等待出现之后获取实际时间
            end_time = time.time()
            log.info('元素--{}--等待成功,耗时：{}秒'.format(locator, end_time - start_time))
            return ele_visibility

    def wait_element_clickable(self, locator, img_info, timeout=20, poll_frequency=0.5):
        '''等待元素可点击'''
        start_time = time.time()
        try:
            element_clickable = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            # 输出日志
            log.error('元素--{}--等待可点击超时'.format(locator))
            log.exception(e)
            # 对当前页面进行截图
            self.save_scree_imge(img_info)
            raise e
        else:
            # 元素等待出现之后获取实际时间
            end_time = time.time()
            log.info('元素--{}--等待可点击成功,耗时：{}秒'.format(locator, end_time - start_time))
            return element_clickable

    def wait_element_presence(self, locator, img_info, timeout=15, poll_frequency=0.5):
        '''等待元素被加载'''
        start_time = time.time()
        try:
            element_presence = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            log.error('元素--{}--加载超时'.format(locator))
            log.exception(e)
            # 元素加载失败时对当前页面进行截图
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('元素--{}--加载成功，耗时：{}秒'.format(locator, end_time - start_time))
            return element_presence

    def get_element_text(self, locator, img_info, timeout=15, poll_frequency=0.5):
        '''获取元素的文本'''
        start_time = time.time()
        try:
            element_text = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)).text
        except Exception as e:
            # 输出日志
            log.error('元素--{}--获取元素文本超时'.format(locator))
            log.exception(e)
            # 获取元素的文本失败时对当前页面进行截图
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('元素--{}--加载成功，耗时：{}秒'.format(locator, end_time - start_time))
            return element_text

    def get_element_attribute(self, locator, attr_name, img_info, timeout=15, poll_frequency=0.5):
        '''获取元素属性'''
        start_time = time.time()
        try:
            element_attribute = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)).get_attribute(attr_name)
        except Exception as e:
            log.error('元素--{}--属性获取超时'.format(locator))
            log.exception(e)
            # 获取元素属性失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('获取元素--{}--属性成功,耗时：{}秒'.format(locator, end_time - start_time))
            return element_attribute

    def click_element(self, locator, img_info, timeout=15, poll_frequency=0.5):
        '''点击元素'''
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            log.error('点击元素--{}--点击失败'.format(locator))
            log.exception(e)
            # 点击失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('点击元素--{}--点击成功,耗时：{}秒'.format(locator, end_time - start_time))

    def input_text(self, locator, text_value, img_info, timeout=15, poll_frequency=0.5):
        '''文本输入'''
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)).send_keys(text_value)
        except Exception as e:
            log.error('输入文本--{}--输入失败'.format(locator))
            log.exception(e)
            # 输入文本失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('输入文本--{}--输入成功,耗时：{}秒'.format(locator, end_time - start_time))

    def get_element(self, locator, img_info, timeout=15, poll_frequency=0.5):
        '''获取元素'''
        start_time = time.time()
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error('获取元素--{}--失败'.format(locator))
            log.exception(e)
            # 获取元素属性失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('获取元素--{}--获取成功,耗时：{}秒'.format(locator, end_time - start_time))
            return element

    def save_scree_imge(self, img_info):
        '''保存截图'''
        start_time = time.time()
        filename = '{}__{}__操作.png'.format(start_time, img_info)
        file_path = os.path.join(ERROR_IMG, filename)
        self.driver.save_screenshot(file_path)
        log.info('错误页面截图成功，图表保存路径：{}'.format(file_path))

    def window_move_element(self, locator, img_info, timeout=20, poll_frequency=0.5):
        '''移动出窗口到指定元素位置'''
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error('滚动窗口到--{}--滚动失败'.format(locator))
            log.exception(e)
            # 滚动失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        return self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def clear_input(self, locator, img_info, timeout=20, poll_frequency=0.5):
        '''清空输入框'''
        start_time = time.time()
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            log.error('清空输入框--{}--失败'.format(locator))
            log.exception(e)
            # 清空失败时进行截图保存
            self.save_scree_imge(img_info)
            raise e
        else:
            end_time = time.time()
            log.info('清空输入框--{}--清除成功,耗时：{}秒'.format(locator, end_time - start_time))
        return element.clear()

    def page_refresh(self):
        '''刷新页面'''
        self.driver.refresh()
