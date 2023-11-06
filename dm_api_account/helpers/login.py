import requests
from dm_api_account.models import AuthenticateViaCredentialsModel


class Login:
    def __init__(self, faced):
        self.faced = faced

    def set_headers(self, headers):
        self.faced.login_api.client.session.headers.update(headers)

    def login_user(self, login: str, password: str, remember_me: bool = True, status_code: int = 200):
        response = self.faced.login_api.post_v1_account_login(
            json=AuthenticateViaCredentialsModel(
                login=login,
                password=password,
                rememberMe=remember_me
            ),
            status_code=status_code
        )
        return response

    def get_auth_token(self, login: str, password: str):
        response = self.login_user(
                                    login=login,
                                    password=password
                                )
        token = {'X-Dm-Auth-Token': response.headers.get('X-Dm-Auth-Token')}
        return token

    def logout_user(self, **kwargs):
        response = self.faced.login_api.delete_v1_account_login(**kwargs)
        return response

    def logout_user_all(self, **kwargs):
        response = self.faced.login_api.delete_v1_account_login_all(**kwargs)
        return response
