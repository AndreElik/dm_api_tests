from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from dm_api_account.helpers.account import Account
from dm_api_account.helpers.login import Login
from dm_api_account.helpers.mailhog import MailHogApi


class Faced:
    def __init__(self, host, mailhog_host=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = MailHogApi()
        self.account = Account(self)
        self.login = Login(self)

