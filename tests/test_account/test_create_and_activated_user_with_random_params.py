import random
from string import ascii_letters, digits
import pytest


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@pytest.mark.parametrize('login, email, password, status_code, check', [
    ('12', '12@12.ru', '123456', 201, ''),
    ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),
    (random_string(1, 1), '12@12.ru', '123456', 400, {"Login": ["Short"]}),
    ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),
    ('12', '12', '123456', 400, {"Email": ["Invalid"]})

])
def test_create_and_activated_user_with_random_params(
        dm_api_faced,
        orm_db,
        login,
        email,
        password,
        status_code,
        check
):
    orm_db.delete_user_by_login(login=login)
    dm_api_faced.mailhog.delete_all_messages()
    response = dm_api_faced.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        dm_api_faced.account.activate_registered_user(login=login)
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert row['Login'] == login, f'user{login} not registered'
            assert row['Activated'] is True, f'user{login} did not activated'
    else:
        assert response.json()["errors"] == check, f'Error message is {response.json()["errors"]}, must be {check}'

