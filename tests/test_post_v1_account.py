from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
import structlog
from time import sleep


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
    json = {
            "login": "user_259",
            "email": "user_259@gmail.com",
            "password": "123456qwerty"
        }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'статус код ответа должен быть 201, но он равен {response.status_code }'
    sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account(token=token)
    assert response.status_code == 200, f'статус код ответа должен быть 200, но он равен {response.status_code}'
    print(response.json())

