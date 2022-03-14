# -*- coding：utf-8 -*-
# @Time ：2022/2/23 22:44
# @Authon :hhj
# @Annotation:
# @File : bid_page.py
from Common.base_page import BasePage
from PageLocators.bidpage_locators import BidPageLocators as loc


class BidPage(BasePage):

    # 投资
    def invest(self, amount):
        doc = '标详情页面_投资操作'
        self.wait_ele_Visible(loc.invest_button, doc=doc)
        # 在输入框中输入金额
        self.input_text(loc.invest_amount_input, amount, doc)
        flag = self.ele_is_enabled(loc.invest_button, doc=doc)
        # print(flag)
        # 判断投标按钮是否为可点击状态，如果为True,就点击投标按钮
        if flag == True:
            self.click_element(loc.invest_button, doc)

    # 获取用户余额
    def get_user_money(self):
        doc = '标详情页面_获取用户余额'
        self.wait_ele_Visible(loc.invest_amount_input, doc=doc)
        return self.get_ele_attribute(loc.invest_amount_input, loc.data_amount, doc)

    # 投资成功的提示框 - 点击关闭按钮，并刷新页面
    def click_closeButton_on_success_popup(self):
        doc = '标详情页面_投资成功的提示框_点击关闭按钮'
        self.wait_ele_Visible(loc.close_pop, doc=doc)
        self.click_element(loc.close_pop, doc)
        self.driver.refresh()

    # 投资成功的提示框 - 点击查看激活
    def click_activeButton_on_success_popup(self):
        doc = '标详情页面_投资成功的提示框_点击查看激活'
        self.wait_ele_Visible(loc.active_button, doc=doc)
        self.click_element(loc.active_button, doc)

    # 修改投资成功弹出框为可见
    def modify_visible_on_success_popup(self):
        js = 'document.querySelector(".pop_capital").style.display = "block";'
        self.driver.execute_script(js)

    # 错误提示框 - 页面中间提示信息
    def get_errorMsg_from_pageCenter(self):
        doc = '标详情页面_页面中央错误提示信息'
        self.wait_ele_Visible(loc.center_confirm_a, doc=doc)
        # 获取文本内容
        error_msg = self.get_text(loc.center_msg_div, doc)
        # 关闭提示框
        self.click_element(loc.center_confirm_a, doc)
        return error_msg

    # 获取提示信息 - 投标按钮上的
    def get_errorMsg_from_investButton(self):
        doc = '标详情页面_页面投标按钮上提示信息'
        self.wait_ele_Visible(loc.invest_button, doc=doc)
        return self.get_text(loc.invest_button, doc)
