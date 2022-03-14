# -*- coding：utf-8 -*-
# @Time ：2022/2/24 21:07
# @Authon :hhj
# @Annotation:
# @File : bidpage_locators.py
from selenium.webdriver.common.by import By


class BidPageLocators:
    # 元素定位
    # 投资金额输入框
    invest_amount_input = (By.XPATH, '//input[contains(@placeholder,"可用余额:")]')
    # 获取可用余额input的属性
    data_amount = 'data-amount'
    # 投标按钮
    # invest_button = (By.XPATH, '//button[text()="投标"]')
    # 投资成功后弹出框中的查看并激活按钮
    active_button = (By.CSS_SELECTOR, '.layui-layer-content>.capital_ts>.capital_btn>button')
    # 投资成功关闭弹出框
    close_pop = (By.CSS_SELECTOR, '.layui-layer-content>.capital_ts>.close_pop>img')
    # 投标按钮
    invest_button = (By.CSS_SELECTOR, '.pd-right>button')
    # 页面中间的提示信息
    center_msg_div = (By.XPATH, '//div[@class="text-center"]')
    # 页面中间的提示框确认按钮
    center_confirm_a = (By.XPATH, '//a[text()="确认"]')
    # 页面中间提示框的关闭按钮
    center_close_a = (By.XPATH, '//span[@class="layui-layer-setwin"]/a')
