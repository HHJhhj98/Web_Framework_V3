# -*- coding：utf-8 -*-
# @Time ：2022/2/22 21:14
# @Authon :hhj
# @Annotation:
# @File : login_datas.py

# 正常场景-测试数据
success_data = [{'user': '17307428595', 'password': 'test123456', 'title': '正常登录'}]

# 异常用例——手机号格式不正确（10位，12位，不在号码段，为空） ddt
phone_data = [{'user': '1730742859', 'password': 'test123456', 'check': '请输入正确的手机号', 'title': '异常用例-输入10位手机号'},
              {'user': '173074285955', 'password': 'test123456', 'check': '请输入正确的手机号', 'title': '异常用例-输入12位手机号'},
              {'user': '', 'password': 'test123456', 'check': '请输入手机号', 'title': '异常用例-手机号为空'},
              {'user': '11607428595', 'password': 'test123456', 'check': '请输入正确的手机号', 'title': '异常用例-手机号不在号码段'},
              {'user': '17307428595', 'password': '', 'check': '请输入密码', 'title': '异常用例-密码为空'}]

# 异常用例——密码不正确（密码不区分大小写，密码过长，密码过短，密码为空）或账号未授权 ddt
phone_pwd_data = [{'user': '17307428595', 'password': 'Test123456', 'check': '帐号或密码错误!', 'title': '异常用例-密码不区分大小写'},
                  {'user': '17307428595', 'password': 'test1234567', 'check': '帐号或密码错误!', 'title': '异常用例-密码过长'},
                  {'user': '17307428595', 'password': 'test12345', 'check': '帐号或密码错误!', 'title': '异常用例-密码过短'},
                  {'user': '17307398595', 'password': 'test123456', 'check': '此账号没有经过授权，请联系管理员!',
                   'title': '异常用例-账号未授权'}]
