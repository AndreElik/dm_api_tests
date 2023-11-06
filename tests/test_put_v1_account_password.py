from time import sleep
from services.dm_api_account import Faced
import structlog


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_password():
    # mailhog = MailHogApi(host='http://5.63.153.31:5025')
    # api = Faced(host='http://5.63.153.31:5051')
    # login = "user_317"
    # password = "123456qwerty"
    # email = "user_317@gmail.com"
    # # json = RegistrationModel(
    # #     login=login,
    # #     email=email,
    # #     password=password
    # # )
    # # api.account.post_v1_account(json=json)
    # # sleep(2)
    # # token = mailhog.get_token_from_last_email()
    # # api.account.put_v1_account(token=token)
    # json = ResetPasswordModel(
    #     login=login,
    #     email=email
    # )
    # api.account_api.post_v1_account_password(json=json)
    # reset_password_token = mailhog.get_token_for_reset_password()
    # json_for_change_password = ChangeRegisteredUserPasswordModel(
    #     login=login, token=reset_password_token,
    #     oldPassword=password, newPassword='124564875'
    #     )
    # response = api.account_api.put_v1_account_password(json=json_for_change_password)
    # print(response.resource.model_dump())
    # assert_that(response.resource, has_properties(
    #     {"login": "user_317",
    #      "roles": [Roles.GUEST, Roles.PLAYER]
    #      }
    # ))
    # assert_that(response.resource.rating, has_properties(
    #     {"enabled": True,
    #      "quality": 0,
    #      "quantity": 0
    #      }
    # ))

    api = Faced(host='http://5.63.153.31:5051')
    login = "user_378"
    email = "user_378@gmail.com"
    password = "123456qwerty"
    new_password = "777qwerty"
    # Register new user
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    sleep(2)
    # Activate registered user
    api.account.activate_registered_user(login=login, status_code=200)
    # Login user
    api.login.login_user(
        login=login,
        password=password)
    # get auth token
    auth_token = api.login.get_auth_token(login=login, password=password)
    # Reset registered  user password
    sleep(2)
    api.account.set_headers(headers=auth_token)
    api.account.reset_registered_user_password(login=login, email=email)
    # Change password
    sleep(2)
    api.account.change_registered_user_password(login=login, password=password, new_password=new_password)

