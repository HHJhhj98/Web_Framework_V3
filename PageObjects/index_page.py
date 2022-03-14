# -*- coding：utf-8 -*-
# @Time ：2022/2/17 23:24
# @Authon :hhj
# @Annotation:
# @File : index_page.py
import random

from PageLocators.indexpage_locators import IndexPageLocators as loc
from Common.base_page import BasePage


class IndexPage(BasePage):

    # 判断是否存在退出链接
    def isExist_logout_ele(self):
        # 如果存在就返回True，如果不存在就返回False
        doc = '首页_退出'
        try:
            # 等待10秒
            self.wait_ele_Visible(loc.sign_out_a, doc=doc)
            return True
        except:
            return False

    # 选标操作 - 默认选择第一个可用的标 - 元素选择时过滤
    def click_first_bid(self):
        doc = '首页_选第一个标'
        self.wait_ele_Visible(loc.bid_a, doc=doc)
        # 找到所有符合条件的标，选择第一个标
        self.click_element(loc.bid_a, doc, index=0)

    # 随机选择一个可用的标
    def click_bid_by_random(self):
        doc = '首页_随机选一个标'
        self.wait_ele_Visible(loc.bid_a, doc=doc)
        # 找到所有符合条件的标
        eles = self.get_elements(loc.bid_a, doc)
        # 随机数
        index = random.randint(0, len(eles) - 1)
        # 选择一个标
        self.click_element(loc.bid_a, doc, index=index)
