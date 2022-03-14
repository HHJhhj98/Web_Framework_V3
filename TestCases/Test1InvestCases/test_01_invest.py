# -*- coding：utf-8 -*-
# @Time ：2022/2/23 21:16
# @Authon :hhj
# @Annotation:
# @File : test_01_invest.py

# 怎样提升用例执行效率？
# 1、使用夹心饼干setUpClass、tearDownClass
# 2、使用接口方式准备测试条件

# 独立的测试账号

# 正常用例
# 前提条件：
##########尽量不要依赖测试环境的数据，如果没有，就自己造环境######
# 1、用户已登录
# 2、有能够投资的标 #如果没有标，则先加标。可以通过接口方式加标。
# 3、用户有可余额
#  1、手动现充值一个亿
#  2、接口方式：查询当前用户还有多少钱。>6000 不用充值。如果小于用例投资的金额，那就充值

# 步骤
# 1、在首页选标 不根据标名，根据抢投标按钮。默认第一个标。
# 标页面-获取一下投资前的用户余额
# 2、标页面-输入投资金额，点击投资按钮
# 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面

# 断言
# 钱  投资后的金额，是不是少了投资的量。
# 个人页面 - 获取投资后的金额
# 投资钱的金额 -投资后的金额 = 投资金额
# 投资记录对不对？
# 利息对不对？#单独设计用例


# 异常用例：非常好创造环境，非常好写的。

# 异常用例：可以不自动化实现，项目上线时手工补测就行
# 全投操作 ? 标的可投金额 > 个人余额
# 投资金额 > 标的可投金额 #满足这种条件标、用户

from TestDatas import bid_datas as BD
from TestDatas import login_datas as LD
from Common.my_log import MyLog
import pytest
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
from PageObjects.index_page import IndexPage

my_log = MyLog()


@pytest.mark.usefixtures("access_web")  # 在运行的时候，会去运行access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestInvest:

    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     my_log.info("====每个用例前置：刷新当前页面====")
    #     self.driver.refresh()
    #
    # @classmethod
    # def setUpClass(cls):
    #     # 每个方法执行之前都会执行
    #     # 前置 访问登录页面,正常登录
    #     my_log.info("====TestInvest用例类前置：初始化浏览器对话，登录前程贷系统====")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #     cls.lg.login(LD.success_data[0]['user'], LD.success_data[0]['password'])
    #     cls.index = IndexPage(cls.driver)
    #     cls.bid = BidPage(cls.driver)
    #     cls.user = UserPage(cls.driver)
    #     cls.index.click_first_bid()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     my_log.info("====TestInvest用例类后置：关闭浏览器会话，清理环境====")
    #     cls.driver.quit()

    @pytest.mark.parametrize("no100_data", BD.no100_data)
    @pytest.mark.demo2
    def test_invest_0_failed_no100(self, access_web, no100_data):
        my_log.info("****异常用例——{}****".format(no100_data['title']))
        bid = BidPage(access_web[0])
        index = IndexPage(access_web[0])
        # access_web[1].login(LD.success_data['user'], LD.success_data['password'])
        # index.click_first_bid()
        bid.invest(no100_data['amount'])
        error_msg = bid.get_errorMsg_from_pageCenter()
        try:
            assert error_msg == no100_data['check']
        except:
            my_log.exception("****异常用例——{}，断言失败！！！****".format(no100_data['title']))
            raise

    @pytest.mark.parametrize("no10_data", BD.no10_data)
    @pytest.mark.demo2
    def test_invest_0_failed_no10(self, access_web, no10_data):
        my_log.info("****异常用例——{}****".format(no10_data['title']))
        bid = BidPage(access_web[0])
        # index = IndexPage(access_web[0])
        # access_web[1].login(LD.success_data['user'], LD.success_data['password'])
        # index.click_first_bid()
        bid.invest(no10_data['amount'])
        error_msg = bid.get_errorMsg_from_investButton()
        try:
            assert error_msg == no10_data['check']
        except:
            my_log.exception("****异常用例——{}，断言失败！！！****".format(no10_data['title']))
            raise

    @pytest.mark.smoke
    @pytest.mark.parametrize("success_data", BD.success_data)
    def test_invest_1_success(self, access_web, success_data):
        my_log.info("****正常用例——{}****".format(success_data['title']))
        bid = BidPage(access_web[0])
        user = UserPage(access_web[0])
        # index = IndexPage(access_web[0])
        # access_web[1].login(LD.success_data['user'], LD.success_data['password'])
        # index.click_first_bid()
        # 步骤
        # 1、在首页选标 不根据标名，根据抢投标按钮。默认第一个标。初始化已实现
        # self.index.click_first_bid()
        # 标页面-获取一下投资前的用户余额
        before_amount = bid.get_user_money()
        # print(before_amount)
        # 2、标页面-输入投资金额，点击投资按钮
        bid.invest(success_data['amount'])
        # 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面
        bid.click_activeButton_on_success_popup()
        # 断言
        # 钱  投资后的金额，是不是少了投资的量。
        # 个人页面 - 获取投资后的金额
        after_amount = user.get_user_money()
        try:
            # 投资前的金额 -投资后的金额 = 投资金额
            assert float(success_data['amount']) == float(before_amount) - float(after_amount)
            # self.assertEqual(float(BD.success_data['amount']), float(before_amount) - float(after_amount))
        except:
            my_log.exception("****正常用例——{}，断言失败！！！****".format(success_data['title']))
            raise
        # 投资记录对不对？
        # 利息对不对？#单独设计用例
