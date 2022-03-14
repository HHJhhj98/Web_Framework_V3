# -*- coding：utf-8 -*-
# @Time ：2022/2/23 0:26
# @Authon :hhj
# @Annotation:
# @File : loginpage_locators.py

from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_but = (By.XPATH, '//button[text()="登录"]')
    # 记住手机号勾选框
    rember_text = (By.XPATH, '//input[@name="remember_me"]')
    # 免费注册入口链接
    register_a = (By.XPATH, '//a[contains(text(),"免费注册")]')
    # 登录区域错误提示框
    login_Area_error_msg = (By.XPATH, '//div[@class="form-error-info"]')
    # 登录页面中央错误提示框
    login_Page_Center_error_msg = (By.XPATH, '//div[@class="layui-layer-content"]')
    # 忘记密码入口链接
    forget_pwd_a = (By.LINK_TEXT, '忘记密码?')
