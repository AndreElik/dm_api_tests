from time import sleep
import structlog
from hamcrest import assert_that, has_properties

from services.dm_api_account import Faced

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)


def test_get_v1_account():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_376"
    email = "user_376@gmail.com"
    password = "123456qwerty"
    # Register new user
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    sleep(2)
    # Activate registered user
    api.account.activate_registered_user(login=login)
    # Login user
    api.login.login_user(
        login=login,
        password=password)
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.account_api.get_v1_account()



