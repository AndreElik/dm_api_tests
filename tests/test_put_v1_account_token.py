from services.dm_api_account import Faced
from dm_api_account.helpers.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_token():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = Faced(host='http://5.63.153.31:5051')
    json = RegistrationModel(
            login="user_293",
            email="user_293@gmail.com",
            password="123456qwerty"
    )
    api.account_api.post_v1_account(json=json)
    sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account_api.put_v1_account_token(token=token)


