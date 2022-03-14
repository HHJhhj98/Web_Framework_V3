# -*- coding：utf-8 -*-
# @Time ：2022/2/23 22:44
# @Authon :hhj
# @Annotation:
# @File : user_page.py

from PageLocators.userpage_locators import UserPageLocators as loc
from Common.base_page import BasePage


class UserPage(BasePage):

    # 个人页面 - 获取可用金额
    def get_user_money(self):
        doc = '个人页面_获取可用金额'
        self.wait_ele_Visible(loc.available_amount_li, doc=doc)
        available_amount = self.get_text(loc.available_amount_li, doc)
        available_amount = available_amount[0: available_amount.index('元')]
        return eval(available_amount)
