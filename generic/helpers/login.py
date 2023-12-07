import allure
from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, faced):
        from services.dm_api_account import Faced
        self.faced: Faced = faced

    def set_headers(
            self,
            headers
    ):
        self.faced.login_api.client.session.headers.update(headers)

    def login_user(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ):
        response = self.faced.login_api.v1_account_login_post(
            login_credentials=LoginCredentials(
                login=login,
                password=password,
                remember_me=remember_me
            )
        )
        return response

    def get_auth_token(
            self,
            login: str,
            password: str):
        response = self.login_user(
            login=login,
            password=password
        )
        with allure.step('Получение токена для авторизации'):
            token = {'X-Dm-Auth-Token': response.headers.get('X-Dm-Auth-Token')}
        return token

    def logout_user(
            self,
            **kwargs
    ):
        response = self.faced.login_api.v1_account_login_delete(**kwargs)
        return response

    def logout_user_all(self, **kwargs):
        response = self.faced.login_api.v1_account_login_all_delete(**kwargs)
        return response
