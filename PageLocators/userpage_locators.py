# -*- coding：utf-8 -*-
# @Time ：2022/2/24 22:07
# @Authon :hhj
# @Annotation:
# @File : userpage_locators.py
from selenium.webdriver.common.by import By


class UserPageLocators:
    # 元素定位
    # 获取可用余额
    available_amount_li = (By.XPATH, '//li[@class="color_sub1"]')
