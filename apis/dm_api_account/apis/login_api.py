import allure
from requests import Response
from ..models import *
from common_libs.restclient import Restclient
from ..models import UserEnvelopeModel
from ..utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(
            host=host,
            headers=headers
        )
        if headers:
            self.client.session.headers.update(headers)

    def delete_v1_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout as current user
        :return:
        """
        with allure.step('Разлогинивание пользователя'):
            response = self.client.delete(
                path=f"/v1/account/login",
                **kwargs
            )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        return response

    def delete_v1_account_login_all(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        Logout from every device
        :return:
        """
        with allure.step('Разлогинивание пользователя со всех устройств'):
            response = self.client.delete(
                path=f"/v1/account/login/all",
                **kwargs
            )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        return response

    def post_v1_account_login(
            self,
            json: AuthenticateViaCredentialsModel,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelopeModel | Response:
        """
        Authenticate via credentials
        :param status_code:
        :param json authenticate_via_credentials_model
        :return:
        """
        with allure.step('Авторизация пользователя'):
            response = self.client.post(
                path=f"/v1/account/login",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        if response.status_code == 200:
            UserEnvelopeModel(**response.json())
        return response
