from dm_api_account.models import AuthenticateViaCredentialsModel


class Login:
    def __init__(self, faced):
        self.faced = faced

    def login_user(self, login: str, password: str, remember_me: bool = True):
        response = self.faced.login_api.post_v1_account_login(
            json=AuthenticateViaCredentialsModel(
                login=login,
                password=password,
                rememberMe=remember_me
            )
        )
        return response

    def get_auth_token(self, login: str, password: str):
        response = self.login_user(
                                    login=login,
                                    password=password
                                )
        token = {'X-Dm-Auth_Token': response.headers['X-Dm-Auth_Token']}
        return token
