from time import sleep
from services.dm_api_account import Faced
import structlog


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_delete_v1_account_login():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_382"
    email = "user_382@gmail.com"
    password = "123456qwerty"
    # Register new user
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    sleep(2)
    # Activate registered user
    api.account.activate_registered_user(login=login, status_code=200)
    # Login user
    api.login.login_user(
        login=login,
        password=password)
    # get auth token
    auth_token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=auth_token)
    api.login.logout_user(headers=auth_token)


