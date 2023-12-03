from hamcrest import assert_that, has_properties
from apis.dm_api_account.models.user_evelope_model import Roles, Rating, UserEnvelopeModel


def test_post_v1_account_login(dm_api_faced, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    response = dm_api_faced.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # api.account.activate_registered_user()
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user{login} not registered'
        assert row['Activated'] is False, f'user{login} was activated'
    orm_db.update_users_activated_field(login=login)

    response = dm_api_faced.login.login_user(
        login=login,
        password=password
    )
    response = UserEnvelopeModel(**response.json())
    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }

    ))
