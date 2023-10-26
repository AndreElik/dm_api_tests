import json
import pprint

import requests
from requests import session, Response
from restclient.restclient import Restclient


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



