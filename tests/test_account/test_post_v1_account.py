import allure
import pytest
import random
from string import ascii_letters, digits


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite('Проверка метода POST/v1/account/password')
@allure.sub_suite('Позитивные проверки ')
class TestPostV1Account:

    @allure.title('Проверка регистрации и активации пользователя')
    def test_post_v1_account(self, dm_api_faced, dm_db, prepare_user, assertions):
        """
        Тест проверяет создание, регистрацию и активацию нового пользователя

        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        dm_api_faced.account.register_new_user(
            login=login,
            email=email,
            password=password
        )
        assertions.check_user_was_created(login=login)
        dm_db.update_users_activated_field(login=login)
        assertions.check_user_was_activated(login=login)
        response = dm_api_faced.login.login_user(
            login=login,
            password=password
        )
        assertions.check_response(response=response, login=login)

    @allure.title('Проверка регистрации и активации пользователя, используя рандомные данные')
    @pytest.mark.parametrize('login, email, password, status_code, check', [
        ('12', '12@12.ru', '123456', 201, ''),
        ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),
        (random_string(1, 1), '12@12.ru', '123456', 400, {"Login": ["Short"]}),
        ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),
        ('12', '12', '123456', 400, {"Email": ["Invalid"]})

    ])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_faced,
            orm_db,
            login,
            email,
            password,
            status_code,
            check,
            assertions
    ):
        """
        Тест проверяет создание, регистрацию и активацию нового пользователя с рандомными параметрами

        """
        orm_db.delete_user_by_login(login=login)
        dm_api_faced.mailhog.delete_all_messages()
        response = dm_api_faced.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            assertions.check_user_was_created(login=login)
            dm_api_faced.account.activate_registered_user(login=login)
            assertions.check_user_was_activated(login=login)
        else:
            assertions.check_response_with_errors(response=response, check=check)
