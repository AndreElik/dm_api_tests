from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel
from dm_api_account.models.change_registered_user_password_model import ChangeRegisteredUserPasswordModel

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_email():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "user_208"
    password = "123456qwerty"
    email = "user_208@gmail.com"
    json = RegistrationModel(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'статус код ответа должен быть 201, но он равен {response.status_code}'
    sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account(token=token)
    assert response.status_code == 200, f'статус код ответа должен быть 200, но он равен {response.status_code}'
    json_for_change_password = ChangeRegisteredUserPasswordModel(
        login=login,
        token=token,
        old_password=password,
        new_password="124456qwerty"
    )
    response = api.account.put_v1_account_password(json=json_for_change_password)
    assert response.status_code == 200, f'статус код ответа должен быть 200, но он равен {response.status_code}'