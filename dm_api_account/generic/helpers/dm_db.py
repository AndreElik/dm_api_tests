class DmDatabase:
    def __init__(self, user, password, host, database):
        connection_string = f'postgresql://{user}:{password}@{host}/{database}'
        self.db = records.Database(connection_string)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')