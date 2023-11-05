from services.dm_api_account import Faced


def test_get_v1_account():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_341"
    password = "123456qwerty"
    token = api.login.get_auth_token(login=login, password=password)
    # api.account_api.get_v1_account()
    print(token)


