
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel
from dm_api_account.models.authenticate_via_credentials_model import AuthenticateViaCredentialsModel


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_post_v1_account_login():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = 'user_223'
    email = 'user_223@gmail.com'
    password = "123456qwerty"
    json = RegistrationModel(
            login=login,
            email=email,
            password=password
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'статус код ответа должен быть 201, но он равен {response.status_code }'
    sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account(token=token)
    assert response.status_code == 200, f'статус код ответа должен быть 200, но он равен {response.status_code}'
    json_for_login = AuthenticateViaCredentialsModel(
            login=login,
            password=password,
            remember_me=True
    )
    response = api.login.post_v1_account_login(json=json_for_login)
    assert response.status_code == 200, f'статус код ответа должен быть 200, но он равен {response.status_code}'
