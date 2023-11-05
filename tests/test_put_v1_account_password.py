from services.dm_api_account import Faced
from dm_api_account.helpers.mailhog import MailHogApi
import structlog
from dm_api_account.models.reset_password_model import ResetPasswordModel
from dm_api_account.models.change_registered_user_password_model import ChangeRegisteredUserPasswordModel
from dm_api_account.models.user_evelope_model import Roles
from hamcrest import assert_that, has_properties


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_password():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_317"
    password = "123456qwerty"
    email = "user_317@gmail.com"
    # json = RegistrationModel(
    #     login=login,
    #     email=email,
    #     password=password
    # )
    # api.account.post_v1_account(json=json)
    # sleep(2)
    # token = mailhog.get_token_from_last_email()
    # api.account.put_v1_account(token=token)
    json = ResetPasswordModel(
        login=login,
        email=email
    )
    api.account_api.post_v1_account_password(json=json)
    reset_password_token = mailhog.get_token_for_reset_password()
    json_for_change_password = ChangeRegisteredUserPasswordModel(
        login=login, token=reset_password_token,
        oldPassword=password, newPassword='124564875'
        )
    response = api.account_api.put_v1_account_password(json=json_for_change_password)
    print(response.resource.model_dump())
    assert_that(response.resource, has_properties(
        {"login": "user_317",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))

