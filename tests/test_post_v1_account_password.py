from dm_api_account.models import ResetPasswordModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.user_evelope_model import Roles
from hamcrest import assert_that, has_properties

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_post_v1_account_password():

    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "user_312"
    password = "123456qwerty"
    email = "user_312@gmail.com"
    json = ResetPasswordModel(
        login=login,
        email=email
    )

    response = api.account.post_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {"login": "user_312",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))





