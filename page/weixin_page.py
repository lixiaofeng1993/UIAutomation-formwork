#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: weixin_page.py
# 说   明: 
# 创建时间: 2020/1/5 14:52
'''
from common.base_page import BasePage


class LoginWeixin(BasePage):
    _more_btn_loc = ("id", "com.tencent.mm:id/cqi")
    _login_other_loc = ("id", "com.tencent.mm:id/cx")
    _weixin_loc = ("id", "com.tencent.mm:id/cqb")
    _user_pass_loc = ("id", "com.tencent.mm:id/l3")
    _login_btn_loc = ("id", "com.tencent.mm:id/cqc")

    def login_wecat(self):
        self.click(self._more_btn_loc)
        self.clicks(self._login_other_loc, 0)
        self.click(self._weixin_loc)
        self.sends_keys(self._user_pass_loc, "cray-L22", 0)
        self.sends_keys(self._user_pass_loc, "fengzi802300", 1)
        self.click(self._login_btn_loc)
