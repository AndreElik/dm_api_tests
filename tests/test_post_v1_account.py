from services.dm_api_account import Faced
import structlog
from time import sleep
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
    login = "user_349"
    email = "user_349@gmail.com"
    password = "123456qwerty"
    # Register new user
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    sleep(2)
    # Activate registered user
    api.account.activate_registered_user()
    # Login user
    api.login.login_user(
        login=login,
        password=password)
    # assert_that(response.resource, has_properties(
    #     {"login": "user_341",
    #      "roles": [Roles.GUEST, Roles.PLAYER]
    #      }
    #
    # ))





