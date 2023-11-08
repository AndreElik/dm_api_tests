from services.dm_api_account import Faced
import structlog
from dm_api_account.models.user_evelope_model import Roles
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)


def test_post_v1_account():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_417"
    email = "user_417@gmail.com"
    password = "123456qwerty"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(
        login=login)
    response = api.login.login_user(
        login=login,
        password=password
    )
    print(response)
    assert_that(response.resource, has_properties(
        {"login": "user_417",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": {"enabled": True,
                    "quality": 0,
                    "quantity": 0
                    }
         }

    ))
