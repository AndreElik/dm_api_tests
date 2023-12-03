from apis.dm_api_account import AccountApi
from apis.dm_api_account import LoginApi
from generic.helpers.account import Account
from generic.helpers.login import Login


class Faced:
    def __init__(self, host, mailhog=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = mailhog
        self.account = Account(self)
        self.login = Login(self)
