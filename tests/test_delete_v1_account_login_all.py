from time import sleep
from services.dm_api_account import Faced
import structlog

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def test_delete_v1_account_login_all():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_388"
    email = "user_388@gmail.com"
    password = "123456qwerty"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    sleep(2)
    api.account.activate_registered_user(
        login=login,
        status_code=200
    )
    api.login.login_user(
        login=login,
        password=password
    )
    auth_token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.login.set_headers(
        headers=auth_token
    )
    api.login.logout_user_all()
