from typing import List

from sqlalchemy.orm import aliased

from dm_api_account.generic.helpers.orm_models import User, Base
from dm_api_account.orm_client.orm_client import OrmClient
from sqlalchemy import select, delete, update, table, column, Table


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_user(self) -> List[User]:
        query = select([User])
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login) -> List[User]:
        query = select([User]).where(User.Login == login)
        print(query)
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        # query = User.__table__.delete().where(User.Login == login)
        query = delete(User).where(User.Login == login)
        print(str(query))
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    def update_users_activated_field(self, login):
        # query = User.__table__.update().where(User.Login == login).values(Activated=True)
        query = update(User).where(User.Login == login).values(Activated=True)
        dataset = self.db.send_bulk_query(query=query)
        return dataset

