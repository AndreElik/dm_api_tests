from hamcrest import assert_that, has_properties
from dm_api_account.models.user_evelope_model import Roles, Rating
from services.dm_api_account import Faced
import structlog

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def test_put_v1_account_password():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_425"
    email = "user_425@gmail.com"
    password = "123456qwerty"
    new_password = "777qwerty"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(
        login=login,
        status_code=200
    )
    api.login.login_user(
        login=login,
        password=password)
    auth_token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(
        headers=auth_token
    )
    api.account.reset_registered_user_password(
        login=login,
        email=email
    )
    response = api.account.change_registered_user_password(
        login=login,
        password=password,
        new_password=new_password
    )
    assert_that(response.resource, has_properties(
        {"login": "user_425",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }

     ))
