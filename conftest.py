import pytest
from collections import namedtuple
from generic.helpers.dm_db import DmDatabase
from generic.helpers.mailhog import MailHogApi
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Faced
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
    mailhog = MailHogApi(host='http://5.63.153.31:5025')
    return mailhog


@pytest.fixture
def dm_api_faced(mailhog):
    api = Faced(host='http://5.63.153.31:5051', mailhog=mailhog)
    return api


@pytest.fixture
def dm_db():
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db


@pytest.fixture
def orm_db():
    db = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    yield db
    db.db.close_connection()


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
