import uuid

import allure
import records
import structlog
from sqlalchemy import create_engine

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


def allure_attach(fn):
    def _wrapper(*args, **kwargs):
        body = str(kwargs.get('query').compile(compile_kwargs={"literal_binds": True}))
        allure.attach(
            body,
            name='request',
            attachment_type=allure.attachment_type.TEXT
        )
        dataset = fn(*args, **kwargs)

        if dataset:
            dataset_text = '; '.join([f'{key.capitalize()}: {value}' for key, value in dataset[0].items()])
            if dataset:
                allure.attach(
                    dataset_text,
                    name='response',
                    attachment_type=allure.attachment_type.TEXT
                )
        return dataset

    return _wrapper


class OrmClient:
    def __init__(self, user, password, host, database):
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'
        self.engine = create_engine(connection_string, isolation_level='AUTOCOMMIT')
        self.db = self.engine.connect()
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    def close_connection(self):
        self.db.close()

    @allure_attach
    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query='query'
        )
        dataset = self.db.execute(statement=query)
        result = [row for row in dataset]
        log.msg(
            event='response',
            dataset=[dict(row) for row in result]
        )
        return result

    @allure_attach
    def send_bulk_query(self, query):
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        self.db.execute(statement=query)

# if __name__ == '__main__':
#     db = DbClient(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
#     query = 'select * from "Users"'
#     db.send_query(query)
