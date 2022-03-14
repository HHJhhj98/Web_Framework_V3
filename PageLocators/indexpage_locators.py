# -*- coding：utf-8 -*-
# @Time ：2022/2/23 22:57
# @Authon :hhj
# @Annotation:
# @File : indexpage_locators.py
from selenium.webdriver.common.by import By


class IndexPageLocators:
    # 元素定位
    # 退出
    sign_out_a = (By.XPATH, '//a[text()="退出"]')
    # 所有符合条件的标
    bid_a = (By.XPATH, '//a[text()="抢投标"]')
