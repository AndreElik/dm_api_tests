import requests
from requests import Response
from ..models.registation_model import RegistrationModel
from ..models.reset_password_model import reset_password_model
from ..models.change_registere_user_email_model import change_registered_user_email_model
from ..models.change_registered_user_password_model import change_registered_user_password_model
from requests import session
from restclient.restclient import Restclient
from dm_api_account.models.user_evelope_model import  UserEnvelopeModel


class AccountApi:
    def __init__(self, host: str, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )

        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        Reset registered user password
        :param json reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :param token
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json()).model_dump(by_alias=True, exclude_none=True)
        return response

    def put_v1_account_email(self, json: change_registered_user_email_model, **kwargs) -> Response:
        """
        Change registered user email
        :param json change_registered_user_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_password(self, json: change_registered_user_password_model, **kwargs) -> Response:
        """
        Change registered user password
        :param json change_registered_user_password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response



