from dm_api_account.generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Faced
import structlog
from dm_api_account.models.user_evelope_model import Roles, Rating
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def test_put_v1_account_email():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_187"
    email = "user_187@gmail.com"
    password = "123456qwerty"
    new_email = "user_376@mail.ru"
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    orm.delete_user_by_login(login=login)
    dataset = orm.get_user_by_login(login=login)
    assert len(dataset) == 0
    api.mailhog.delete_all_messages()
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = orm.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user{login} not registered'
        assert row['Activated'] is False, f'user{login} was activated'
    orm.update_users_activated_field(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
    token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.account.set_headers(
        headers=token
    )
    response = api.account.change_registered_user_email(
        login=login,
        email=new_email,
        password=password
    )
    assert_that(response.resource, has_properties(
        {"login": "user_187",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }

    ))
