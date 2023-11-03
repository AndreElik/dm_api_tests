from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep
from dm_api_account.models.registation_model import RegistrationModel


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
            login="user_301",
            email="user_301@gmail.com",
            password="123456qwerty"
    )
    api.account.post_v1_account(json=json, status_code=201)
    sleep(2)
    mailhog.get_token_from_last_email()




