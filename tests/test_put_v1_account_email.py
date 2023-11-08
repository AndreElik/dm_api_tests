from services.dm_api_account import Faced
import structlog
from dm_api_account.models.user_evelope_model import Roles
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def test_put_v1_account_email():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_187"
    email = "user_187@gmail.com"
    password = "123456qwerty"
    new_email = "user_376@mail.ru"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(
        login=login
    )
    api.login.login_user(
        login=login,
        password=password
    )
    token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(
        headers=token
    )
    response = api.account.change_registered_user_email(
        login=login,
        email=new_email,
        password=password
    )
    assert_that(response.resource, has_properties(
        {"login": "user_187",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": {"enabled": True,
                    "quality": 0,
                    "quantity": 0
                    }
         }

    ))
