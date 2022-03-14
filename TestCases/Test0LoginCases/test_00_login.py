# -*- coding：utf-8 -*-
# @Time ：2022/2/17 23:25
# @Authon :hhj
# @Annotation:
# @File : test_login_t.py
import allure
import pytest

from TestDatas import login_datas as LD
from Common.my_log import MyLog
from PageObjects.index_page import IndexPage

my_log = MyLog()


# @pytest.mark.demo
# def test_demo():
#     my_log.info("TTTTTTTTTTTTTTTT")


@pytest.mark.usefixtures("access_web")  # 在运行的时候，会去运行access_web函数
@pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # @classmethod
    # def setUpClass(cls):
    #     # 类方法执行之前执行 setUpClass->test1->test2-tearDownClass
    #     # 1、所有用例执行之前，打开浏览器，访问登录页面；2、每个页面操作完成之后，刷新当前页面；3、最后一个用例是登录成功的用例
    #     # 前置 访问登录页面
    #     my_log.info("====TestLogin用例类前置：初始化浏览器对话，登录前程贷系统====")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #     cls.index = IndexPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     my_log.info("====TestLogin用例类后置：关闭浏览器会话，清理环境====")
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     # 每个方法执行之前都会执行
    #     # 前置 访问登录页面
    #     # self.driver = webdriver.Chrome()
    #     # self.driver.get(CD.web_login_url)
    #     # self.lg = LoginPage(self.driver)
    #     # self.index = IndexPage(self.driver)
    #     pass
    #
    # def tearDown(self):
    #     # 后置 每个方法执行完毕之后都会执行
    #     # self.driver.quit()
    #     self.driver.refresh()

    # 异常用例——手机号格式不正确（10位，12位，不在号码段，为空） ddt
    @pytest.mark.parametrize("phone_data", LD.phone_data)
    @pytest.mark.demo1
    def test_login_0_user_wrongFormat(self, access_web, phone_data):
        my_log.info("****异常用例——{}****".format(phone_data['title']))
        # 步骤 输入用户名：Xxx 密码：XXX 点击登录
        access_web[1].login(phone_data['user'], phone_data['password'])
        try:
            # 登录页面获取提示框文本值
            # 断言 比对文本内容与预期的值是否相等
            # self.assertEqual(access_web[1].get_errorMsg_from_loginArea(), phone_data['check'])
            assert access_web[1].get_errorMsg_from_loginArea() == phone_data['check']
        except:
            my_log.exception("****异常用例——{}，断言失败！！！****".format(phone_data['title']))
            raise

    # 异常用例——密码不正确（密码不区分大小写，密码过长，密码过短，为空）或账号未授权 ddt
    @pytest.mark.parametrize("phone_pwd_data", LD.phone_pwd_data)
    @pytest.mark.demo1
    def test_login_0_wrongPwd_noReg(self, access_web, phone_pwd_data):
        my_log.info("****异常用例——{}****".format(phone_pwd_data['title']))
        # 步骤 输入用户名：Xxx 密码：XXX 点击登录
        access_web[1].login(phone_pwd_data['user'], phone_pwd_data['password'])
        try:
            # 登录页面中央获取提示框文本值
            # 断言 比对文本内容与预期的值是否相等
            # self.assertEqual(access_web[1].get_errorMsg_from_loginPageCenter(), phone_pwd_data['check'])
            assert access_web[1].get_errorMsg_from_loginPageCenter() == phone_pwd_data['check']
        except:
            my_log.exception("****异常用例——{}，断言失败！！！****".format(phone_pwd_data['title']))
            raise

    # 正常用例——登录成功
    @pytest.mark.parametrize("success_data", LD.success_data)
    @pytest.mark.smoke3
    def test_login_1_success(self, access_web, success_data):  # fixture的函数名称作为用例参数，用来接收fixture的返回值
        my_log.info("****正常用例——{}****".format(success_data['title']))
        # 步骤 输入用户名：Xxx 密码：XXX 点击登录
        access_web[1].login(success_data['user'], success_data['password'])
        # 断言 首页中能否找到退出元素
        try:
            with allure.step("step6：断言是否存在退出链接"):
                # assert IndexPage(access_web[0]).isExist_logout_ele()
                assert False
        except:
            my_log.exception("****正常用例——{}，断言失败！！！****".format(success_data['title']))
            raise

    # # 异常用例——用户名为空
    # def test_login_noUser(self):
    #     # 步骤 输入用户名：Xxx 密码：XXX 点击登录
    #     self.lg.login("", "test12345678")
    #     # 断言 登录页面提示：请输入手机号
    #     self.assertTrue(self.lg.isExist_login_noUser_ele())

    # 异常用例——手机号未注册
    # 异常用例——错误的密码
    # 异常用例——不输入密码

# pagelocators-pageobjects
# testcases=pageobjects+testdatas
# 单向调用
# 1、数据分离 TestDatas
# 2、测试用例ddt引用
# 3、优化了setUpClass、tearDownClass，每条测试用例之间要互不影响
# 4、元素定位分离：元素定位类型和元素定位表达式用元组管理，PageLocators层
