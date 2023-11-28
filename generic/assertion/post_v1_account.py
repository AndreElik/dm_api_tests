import allure
from hamcrest import assert_that, has_properties

from dm_api_account.models.user_evelope_model import Roles, Rating, UserEnvelopeModel
from generic.helpers.dm_db import DmDatabase
from generic.helpers.orm_db import OrmDatabase


class AssertionsPostV1Account:
    def __init__(self, db: DmDatabase | OrmDatabase ):
        self.db = db

    def check_user_was_created(self, login):
        with allure.step('Проверка создания пользователя'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert row['Login'] == login, f'user{login} not registered'
                assert row['Activated'] is False, f'user{login} was activated'

    def check_user_was_activated(self, login):
        with allure.step('Проверка активации пользователя'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert row['Activated'] is True, f'user{login} not activated'

    def check_response(self, response, login):
        with allure.step('Проверка ответа сервера'):
            response = UserEnvelopeModel(**response.json())
            assert_that(response.resource, has_properties(
                {"login": login,
                 "roles": [Roles.GUEST, Roles.PLAYER],
                 "rating": Rating(enabled=True,
                                  quality=0,
                                  quantity=0)
                 }

            ))

    def check_response_with_errors(self, response, check):
        with allure.step('Проверка сообщения об ошибки'):
            assert response.json()["errors"] == check, \
                f'Error message is {response.json()["errors"]}, must be {check}'

