import requests
from serviceces.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount()
    json = {
            "login": "user_252",
            "email": "user_252@gmail.com",
            "password": "123456qwerty"
        }
    response = api.account.post_v1_account(json=json)
    print(response)

