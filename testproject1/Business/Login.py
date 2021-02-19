# coding=utf-8
# 导入selenium封装类
from Commonlib.Commonlib import Commonshare


class Login(Commonshare):
    def login(self, user, pwd):
        self.open_url('http://localhost:8013/iwebshop/')
        self.click('css', '.loginfo>a')
        self.input_data('name', 'login_info', user)
        self.input_data('name', 'password', pwd)
        self.click('class', 'submit_login')
        self.brown()

if __name__ == '__main__':
    log = Login()
    log.login('laopi', '123456')