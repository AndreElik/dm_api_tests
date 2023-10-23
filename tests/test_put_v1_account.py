import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    token = '564e9e0e-3232-4f00-ac72-056f616aabd6'
    response = api.account.put_v1_account(token=token)
    print(response)


