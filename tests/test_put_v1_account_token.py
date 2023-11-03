from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_token():
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = RegistrationModel(
            login="user_293",
            email="user_293@gmail.com",
            password="123456qwerty"
    )
    api.account.post_v1_account(json=json)
    sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account.put_v1_account(token=token)


