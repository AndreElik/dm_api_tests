from model import Registration


class Account:
    def __init__(self, faced):
        self.faced = faced

    def register_new_user(self, login: str, email: str, password: str):
        response = self.faced.account_api.post_v1_account(
            json=Registration(login=login,
                              email=email,
                              password=password)
        )
        return response

    def activate_registered_user(self):
        token = self.faced.mailhog.get_token_from_last_email()
        response = self.faced.account_api.put_v1_account_token(
            token=token)

        return response
