# -*- coding：utf-8 -*-
# @Time ：2022/2/27 18:16
# @Authon :hhj
# @Annotation:
# @File : conftest.py

# 声明它是一个fixture
import pytest
from selenium import webdriver

from Common.my_log import MyLog
from PageObjects.bid_page import BidPage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from PageObjects.user_page import UserPage
from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD

my_log = MyLog()
driver = None


@pytest.fixture(scope='class')
def access_web():
    '''The scope for which this fixture is shared; one of ``"function(setUp/teardown)"``
            (default), ``"class(setUpClass/teardownClass)"``, ``"module"``, ``"package"`` or ``"session"``.'''
    global driver
    # 前置操作
    my_log.info("====所有用例的前置操作：初始化浏览器对话，登录前程贷系统(setUpClass)====")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    lg.login(LD.success_data[0]['user'], LD.success_data[0]['password'])
    index = IndexPage(driver)
    # bid = BidPage(driver)
    # user = UserPage(driver)
    index.click_first_bid()
    yield (driver, lg)  # 分割线，返回值
    # 后置操作
    my_log.info("====所有用例的后置操作：关闭浏览器会话，清理环境(teardownClass)====")
    driver.quit()


@pytest.fixture(scope='function')
def refresh_page():
    global driver
    # 前置操作
    my_log.info("====每条用例的前置操作：用例开始执行(setUP)====")
    yield
    # 后置操作
    my_log.info("====每条用例的后置操作：用例执行完毕，刷新界面(teardown)====")
    driver.refresh()
# # 单个标签定义
# def pytest_configure(config):
#     config.addinivalue_line("markers", "smoke")  # smoke是标签名


# # 多个标签定义
# def pytest_configure_all(config):
#     marker_list = ["smoke", "demo"]
#     for markers in marker_list:
#         config.addinivalue_line("markers", markers)
