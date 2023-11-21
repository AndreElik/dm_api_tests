from db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_user(self):
        query = 'select * from "Users"'
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):
        query = f'''
        select * from "Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        query = f'''
        delete from "Users" where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    def update_users_activated_field(self, login):
        query = f'''
        update "Users" set "Activated" = True where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset
