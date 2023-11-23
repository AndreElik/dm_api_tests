from hamcrest import assert_that, has_properties
from dm_api_account.models.user_details_envelope_models import Roles


def test_get_v1_account(dm_api_faced, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_faced.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'user{login} not registered'
        assert row['Activated'] is False, f'user{login} was activated'
    orm_db.update_users_activated_field(login=login)
    dm_api_faced.login.login_user(
        login=login,
        password=password)
    token = dm_api_faced.login.get_auth_token(login=login, password=password)
    dm_api_faced.account.set_headers(headers=token)
    response = dm_api_faced.account_api.get_v1_account()

    assert_that(response.resource, has_properties(
        {"login": login,
         "roles": [Roles.GUEST, Roles.PLAYER],
         "info": ''
         }

    ))




