import allure


@allure.suite('Проверка метода PUT/v1/account/token')
@allure.sub_suite('Позитивные проверки ')
class TestPutV1AccountToken:

    @allure.title('Проверка активации пользователя')
    def test_put_v1_account_token(
            self,
            dm_api_faced,
            orm_db,
            prepare_user,
            assertions
    ):
        """
        Позитивный тест активации пользователя

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
        dm_api_faced.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)
