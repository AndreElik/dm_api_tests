
def test_delete_v1_account_login_all(dm_api_faced, orm_db, prepare_user):
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
        password=password
    )
    auth_token = dm_api_faced.login.get_auth_token(
        login=login,
        password=password
    )
    dm_api_faced.login.set_headers(
        headers=auth_token
    )
    dm_api_faced.login.logout_user_all()
