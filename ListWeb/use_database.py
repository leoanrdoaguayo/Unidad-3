import psycopg2
import psycopg2.extras
from config import config


class UseDatabase:
    def __init__(self):
        """Constructor"""
        self.params = config()

    def __enter__(self) -> 'cursor':
        self.connection = psycopg2.connect(**self.params)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
