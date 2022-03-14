# -*- coding：utf-8 -*-
# @Time ：2022/2/24 21:37
# @Authon :hhj
# @Annotation:
# @File : bid_datas.py

# 正常投资
success_data = [{'amount': '100.00', 'title': '正常投资'}]

# 异常投资 - 非100的整数倍
no100_data = [{'amount': '110.00', 'check': '投标金额必须为100的倍数', 'title': '异常投资 - 非100的整数倍_110'},
              {'amount': '280.00', 'check': '投标金额必须为100的倍数', 'title': '异常投资 - 非100的整数倍_280'}]

# 异常投资 - 非10的整数倍
no10_data = [{'amount': '111.00', 'check': '请输入10的整数倍', 'title': '异常投资 - 非100的整数倍_111'},
             {'amount': '28.00', 'check': '请输入10的整数倍', 'title': '异常投资 - 非100的整数倍_28'}]
