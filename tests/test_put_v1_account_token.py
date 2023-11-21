import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.user_evelope_model import Roles, Rating
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Faced

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account_token():
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_349"
    email = "user_349@gmail.com"
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
    response = api.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }

    ))

