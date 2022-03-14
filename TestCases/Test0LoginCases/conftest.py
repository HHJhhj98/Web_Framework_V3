# -*- coding：utf-8 -*-
# @Time ：2022/2/27 18:16
# @Authon :hhj
# @Annotation:
# @File : conftest.py

# 声明它是一个fixture
import allure
import pytest
from selenium import webdriver
import os
from Common.my_log import MyLog
from PageObjects.login_page import LoginPage
from TestDatas import Common_Datas as CD

my_log = MyLog()
driver = None


@pytest.fixture(scope='class')
def access_web():
    '''The scope for which this fixture is shared; one of ``"function(setUp/teardown)"``
            (default), ``"class(setUpClass/teardownClass)"``, ``"module"``, ``"package"`` or ``"session"``.'''
    global driver
    # 前置操作
    my_log.info("====所有用例的前置操作：初始化浏览器对话，登录前程贷系统(setUp)====")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)  # 分割线，返回值
    # 后置操作
    my_log.info("====所有用例的后置操作：关闭浏览器会话，清理环境(teardown)====")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='function')
def refresh_page():
    global driver
    # 前置操作
    yield
    # 后置操作
    my_log.info("====每条用例的后置操作：关闭浏览器会话，清理环境(teardownClass)====")
    driver.refresh()

# # 单个标签定义
# def pytest_configure(config):
#     config.addinivalue_line("markers", "smoke")  # smoke是标签名


# # 多个标签定义
# def pytest_configure_all(config):
#     marker_list = ["smoke", "demo"]
#     for markers in marker_list:
#         config.addinivalue_line("markers", markers)
