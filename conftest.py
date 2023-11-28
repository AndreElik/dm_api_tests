from collections import namedtuple

import allure
import pytest

from generic.assertion.post_v1_account import AssertionsPostV1Account
from generic.helpers.dm_db import DmDatabase
from generic.helpers.mailhog import MailHogApi
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Faced
from pathlib import Path
from vyper import v
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )
    ]
)


@pytest.fixture
def mailhog():
    mailhog = MailHogApi(host=v.get('service.mailhog'))
    return mailhog


@pytest.fixture
def dm_api_faced(mailhog):
    api = Faced(host=v.get('service.dm_api_account'), mailhog=mailhog)
    return api


options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5'
)


@pytest.fixture
def dm_db():
    db = DmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture
def orm_db():
    db = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    yield db
    db.db.close_connection()


@pytest.fixture()
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)


@pytest.fixture()
def assertions_with_orm_db(orm_db):
    return AssertionsPostV1Account(orm_db)


@allure.step('Подготовка нового пользователя')
@pytest.fixture
def prepare_user(dm_api_faced, dm_db):
    login = "user_476"
    email = "user_476@gmail.com"
    password = "123456qwerty"
    new_email = "user_376@mail.ru"
    new_password = "777qwerty"
    dm_api_faced.mailhog.delete_all_messages()
    dm_db.delete_user_by_login(login=login)
    user = namedtuple('User', 'login, email, password, new_email, new_password')
    User = user(login=login, email=email, password=password, new_email=new_email, new_password=new_password)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    return User


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
