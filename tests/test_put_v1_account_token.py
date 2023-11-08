import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_evelope_model import Roles
from services.dm_api_account import Faced

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_token():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_349"
    email = "user_349@gmail.com"
    password = "123456qwerty"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    response = api.account.activate_registered_user()
    assert_that(response.resource, has_properties(
        {"login": "user_349",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))


