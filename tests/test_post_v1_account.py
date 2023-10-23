import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
            "login": "user_252",
            "email": "user_252@gmail.com",
            "password": "123456qwerty"
        }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)

