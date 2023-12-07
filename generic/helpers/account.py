import allure
from dm_api_account.models import ResetPassword, ChangePassword, ChangeEmail
from dm_api_account.models import Registration


class Account:
    def __init__(self, faced):
        from services.dm_api_account import Faced
        self.faced:Faced = faced

    def set_headers(
            self,
            headers
    ):
        self.faced.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str
    ):
        with allure.step('Регистрация пользователя'):
            response = self.faced.account_api.register(
                registration=Registration(
                    login=login,
                    email=email,
                    password=password
                )
            )
        return response

    def activate_registered_user(
            self,
            login: str
    ):
        token = self.faced.mailhog.get_token_by_login(
            login=login
        )
        with allure.step('Активация зарегистрированного пользователя'):
            response = self.faced.account_api.activate(
                token=token
            )

        return response

    def get_current_user_info(
            self,
            **kwargs
    ):
        with allure.step('Получение данных пользователя'):
            response = self.faced.account_api.get_current(**kwargs)
            return response

    def reset_registered_user_password(
            self,
            login: str,
            email: str,
            status_code: int = 200,
            **kwargs
    ):
        with allure.step('Сброс пароля'):
            response = self.faced.account_api.reset_password(
                reset_password=ResetPassword(
                    login=login,
                    email=email),
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
            response = self.faced.account_api.change_password(
                change_password=ChangePassword(
                    login=login,
                    token=token,
                    old_password=password,
                    new_password=new_password),
                **kwargs
            )
        return response

    def change_registered_user_email(
            self,
            login: str,
            password: str,
            email: str,
            **kwargs
    ):
        with allure.step('Смена электронного адреса'):
            response = self.faced.account_api.change_email(
                change_email=ChangeEmail(
                    login=login,
                    password=password,
                    email=email),
                **kwargs
            )
        return response
