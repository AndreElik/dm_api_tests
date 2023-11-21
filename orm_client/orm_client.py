import uuid
import records
import structlog
from sqlalchemy import create_engine

structlog.configure(
    processors=[structlog.processors.JSONRenderer(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )])


class OrmClient:
    def __init__(self, user, password, host, database):
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'
        self.engine = create_engine(connection_string, isolation_level='AUTOCOMMIT')
        self.db = self.engine.connect()
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    def close_connection(self):
        self.db.close()

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

