from typing import Any

import allure
from requests import Response
from ..models import *
from common_libs.restclient import Restclient
from dm_api_account.utilities import validate_request_json, validate_status_code
from ..models import UserDetailsEnvelopeModel


class AccountApi:
    def __init__(self, host: str, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(
            host=host,
            headers=headers
        )
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(
            self,
            json: RegistrationModel,
            status_code=201,
            **kwargs
    ) -> Response:
        """
        :param status_code:
        :param json registration_model
        Register new user
        :return:
        """
        with allure.step('Регистрация пользователя'):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> UserDetailsEnvelopeModel | Any:
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(
            response,
            status_code=status_code
        )
        if response.status_code == 200:
            return UserDetailsEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(
            self,
            json: ResetPasswordModel,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        """
        Reset registered user password
        :param status_code:
        :param json reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        """
        Activate registered user
        :param status_code
        :param token
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(
            self,
            json: ChangeRegisteredUserEmailModel,
            status_code=200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        """
        Change registered user email
        :param status_code
        :param json change_registered_user_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())

        return response

    def put_v1_account_password(
            self,
            json: ChangeRegisteredUserPasswordModel,
            status_code=200,
            **kwargs
    ) -> Response | UserEnvelopeModel:
        """
        Change registered user password
        :param status_code
        :param json change_registered_user_password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(
            response=response,
            status_code=status_code
        )
        if response.status_code == 200:
            return UserEnvelopeModel(**response.json())
        return response
