import json
import pprint
import time

import requests
from requests import session, Response
from restclient.restclient import Restclient

def decorator(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 1:
                print(f'attempt{i}')
                time.sleep(2)
                continue
            else:
                return response
    return wrapper


class MailHogApi:
    def __init__(self, host='http://5.63.153.31:5025') :
        self.host = host
        self.client = Restclient(host=host)
        # self.account = AccountApi(host, headers)
        # self.login = LoginApi(host, headers)

    def get_api_v2_messages(self, limit=50) -> Response:
        """
        Get message by limit
        :param limit:
        :return:
        """

        response = self.client.get(
            path=f"/api/v2/messages",
            params={'limit': limit}
        )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        email = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(email['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
        token = token_url.split('/')[-1]
        return token

    def get_token_for_reset_password(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        email = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(email['items'][0]['Content']['Body'])['ConfirmationLinkUri']
        token = token_url.split('/')[-1]
        return token

    def get_token_by_login(self, login: str, attempt=50):
        if attempt == 0:
            raise AssertionError(f'Не удалось получить письмо с логином{login}')
        emails = self.get_api_v2_messages(limit=100).json()['items']
        for email in emails:
            user_data = json.loads(email['Content']['Body'])
            if login == user_data.get('Login'):
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                return token
        time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt -1):




