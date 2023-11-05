from services.dm_api_account import Faced
from dm_api_account.helpers.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel
from dm_api_account.models.authenticate_via_credentials_model import AuthenticateViaCredentialsModel
from dm_api_account.models.user_evelope_model import Roles
from hamcrest import assert_that, has_properties


structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = Faced(host='http://5.63.153.31:5051')
    login = 'user_304'
    email = 'user_304@gmail.com'
    password = "123456qwerty"
    json = RegistrationModel(
            login=login,
            email=email,
            password=password
    )
    api.account_api.post_v1_account(json=json, status_code=201)
    sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account_api.put_v1_account_token(token=token)
    json_for_login = AuthenticateViaCredentialsModel(
            login=login,
            password=password,
            remember_me=True
    )
    response = api.login_api.post_v1_account_login(json=json_for_login, status_code=200)
    assert_that(response.resource, has_properties(
        {"login": "user_304",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))

