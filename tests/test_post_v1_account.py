from dm_api_account.generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Faced
import structlog
from dm_api_account.models.user_evelope_model import Roles, Rating, UserEnvelopeModel
from hamcrest import assert_that, has_properties

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
    api = Faced(host='http://5.63.153.31:5051')
    login = "user_476"
    email = "user_476@gmail.com"
    password = "123456qwerty"
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user{login} not registered'
        assert row['Activated'] is False, f'user{login} was activated'
    db.update_users_activated_field(login=login)
    # api.account.activate_registered_user(
    #     login=login)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'user{login} not activated'
    response = api.login.login_user(
        login=login,
        password=password
    )
    response = UserEnvelopeModel(**response.json())
    assert_that(response.resource, has_properties(
        {"login": "user_476",
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }


    ))
