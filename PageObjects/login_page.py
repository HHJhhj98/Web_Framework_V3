# -*- coding：utf-8 -*-
# @Time ：2022/2/17 22:48
# @Authon :hhj
# @Annotation:
# @File : login_page.py
import allure

from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.base_page import BasePage


class LoginPage(BasePage):

    # 登录操作
    def login(self, phone, password, rember_user=True):
        doc = '登录页面_登录功能'
        with allure.step("step1：等待登录按钮可见"):
            self.wait_ele_Visible(loc.login_but, doc=doc)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.login_but))
        with allure.step("step2：在{0}中输入用户名：{1}".format(loc.name_text, phone)):
            self.input_text(loc.name_text, phone, doc)
        # self.driver.find_element(*loc.name_text).send_keys(phone)
        with allure.step("step3：在{0}中输入密码：{1}".format(loc.pwd_text, password)):
            self.input_text(loc.pwd_text, password, doc)
        # self.driver.find_element(*loc.pwd_text).send_keys(password)
        if rember_user != True:
            # 判断rember_user的值为False，取消勾选记住密码
            # 否则为默认勾选
            with allure.step("step4：取消勾选记住密码"):
                self.click_element(loc.rember_text, doc)
            # self.driver.find_element(*loc.rember_text).click()
        else:
            with allure.step("step4：勾选记住密码"):
                pass
        with allure.step("step5：点击登录按钮"):
            self.click_element(loc.login_but, doc)
        # self.driver.find_element(*loc.login_but).click()

    # 注册入口
    def register_enter(self):
        doc = '登录页面_注册入口'
        self.wait_ele_Visible(loc.register_a, doc=doc)
        self.click_element(loc.register_a, doc)

    # 忘记密码
    def forget_pwd_enter(self):
        doc = '登录页面_忘记密码入口'
        self.wait_ele_Visible(loc.forget_pwd_a, doc)
        self.click_element(loc.forget_pwd_a, doc)

    # 获取错误提示信息-登录区域
    def get_errorMsg_from_loginArea(self):
        doc = '登录页面_获取登录区域错误提示信息'
        self.wait_ele_Visible(loc.login_Area_error_msg, doc=doc)
        return self.get_text(loc.login_Area_error_msg, doc)

    # 获取错误提示信息-页面正中央
    def get_errorMsg_from_loginPageCenter(self):
        doc = '登录页面_获取页面正中央错误提示信息'
        self.wait_ele_Visible(loc.login_Page_Center_error_msg, doc=doc)
        return self.get_text(loc.login_Page_Center_error_msg, doc)
