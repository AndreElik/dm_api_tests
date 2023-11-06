from time import sleep
from services.dm_api_account import Faced
import structlog


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_post_v1_account_password():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_378"
    email = "user_378@gmail.com"
    password = "123456qwerty"
    new_password = "777qwerty"
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
    # Reset registered  user password
    sleep(2)
    api.account.set_headers(headers=auth_token)
    api.account.reset_registered_user_password(login=login, email=email)

    # assert_that(response.resource, has_properties(
    #     {"login": "user_312",
    #      "roles": [Roles.GUEST, Roles.PLAYER]
    #      }
    # ))
    # assert_that(response.resource.rating, has_properties(
    #     {"enabled": True,
    #      "quality": 0,
    #      "quantity": 0
    #      }
    # ))





