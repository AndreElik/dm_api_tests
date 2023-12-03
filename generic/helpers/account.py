import allure

from apis.dm_api_account.models import ResetPasswordModel, ChangeRegisteredUserPasswordModel, ChangeRegisteredUserEmailModel
from apis.dm_api_account import RegistrationModel


class Account:
    def __init__(self, faced):
        self.faced = faced

    def set_headers(
            self,
            headers
    ):
        self.faced.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str,
            status_code: int = 201
    ):
        with allure.step('Регистрация пользователя'):
            response = self.faced.account_api.post_v1_account(
                json=RegistrationModel(
                    login=login,
                    email=email,
                    password=password
                ),
                status_code=status_code
            )
        return response

    def activate_registered_user(
            self,
            login: str,
            status_code: int = 200
    ):
        token = self.faced.mailhog.get_token_by_login(
            login=login
        )
        with allure.step('Активация зарегистрированного пользователя'):
            response = self.faced.account_api.put_v1_account_token(
                token=token,
                status_code=status_code
            )

        return response

    def get_current_user_info(
            self,
            **kwargs
    ):
        with allure.step('Получение данных пользователя'):
            response = self.faced.account_api.get_v1_account(**kwargs)
            return response

    def reset_registered_user_password(
            self,
            login: str,
            email: str,
            status_code: int = 200,
            **kwargs
    ):
        with allure.step('Сброс пароля'):
            response = self.faced.account_api.post_v1_account_password(
                json=ResetPasswordModel(
                    login=login,
                    email=email),
                status_code=status_code,
                **kwargs)
        return response

    def change_registered_user_password(
            self,
            login: str,
            password: str,
            new_password: str,
            status_code: int = 200,
            **kwargs
    ):
        token = self.faced.mailhog.get_token_for_reset_password(
            login=login
        )
        with allure.step('Смена пароля'):
            response = self.faced.account_api.put_v1_account_password(
                json=ChangeRegisteredUserPasswordModel(
                    login=login,
                    token=token,
                    oldPassword=password,
                    newPassword=new_password),
                status_code=status_code,
                **kwargs
            )
        return response

    def change_registered_user_email(
            self,
            login: str,
            password: str,
            email: str,
            status_code: int = 200,
            **kwargs
    ):
        with allure.step('Смена электронного адреса'):
            response = self.faced.account_api.put_v1_account_email(
                json=ChangeRegisteredUserEmailModel(
                    login=login,
                    password=password,
                    email=email),
                status_code=status_code,
                **kwargs
            )
        return response
