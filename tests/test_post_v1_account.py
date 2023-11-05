from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel
from dm_api_account.models.user_evelope_model import User, Roles, Rating
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
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = RegistrationModel(
            login="user_338",
            email="user_338@gmail.com",
            password="123456qwerty"
    )
    api.account.post_v1_account(json=json, status_code=201)
    sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account(token=token, status_code=200)

    assert_that(response.resource, has_properties(
        {"login": "user_338",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "enabled": True
         }

    ))





