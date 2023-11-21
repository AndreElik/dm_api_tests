from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Faced
import structlog

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def test_delete_v1_account_login_all():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_388"
    email = "user_388@gmail.com"
    password = "123456qwerty"
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
    auth_token = api.login.get_auth_token(
        login=login,
        password=password
    )
    api.login.set_headers(
        headers=auth_token
    )
    api.login.logout_user_all()
