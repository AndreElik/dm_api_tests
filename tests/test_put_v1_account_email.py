from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel
from dm_api_account.models.change_registere_user_email_model import ChangeRegisteredUserEmailModel
from dm_api_account.models.user_evelope_model import User, Roles, Rating
from hamcrest import assert_that, has_properties

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_email():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "user_407"
    password = "123456qwerty"
    json = RegistrationModel(
        login=login,
        email="user_407@gmail.com",
        password=password
    )
    api.account.post_v1_account(json=json, status_code=201)
    sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account(token=token, status_code=200)
    json_for_change_email = ChangeRegisteredUserEmailModel(
        login=login,
        email="user_405@gmail.com",
        password=password
    )
    response = api.account.put_v1_account_email(json=json_for_change_email)
    assert_that(response.resource, has_properties(
        {"login": "user_407",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))




