from hamcrest import assert_that, has_properties
from dm_api_account.models.user_evelope_model import Roles, Rating


def test_put_v1_account_token(dm_api_faced, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_faced.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    response = dm_api_faced.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [Roles.GUEST, Roles.PLAYER],
         "rating": Rating(enabled=True,
                          quality=0,
                          quantity=0)
         }

    ))

