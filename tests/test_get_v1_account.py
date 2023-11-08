import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_details_envelope_models import Roles
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
    login = "user_412"
    email = "user_412@gmail.com"
    password = "123456qwerty"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password)
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    response = api.account_api.get_v1_account()

    assert_that(response.resource, has_properties(
        {"login": "user_412",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "info": ''
         }

    ))




