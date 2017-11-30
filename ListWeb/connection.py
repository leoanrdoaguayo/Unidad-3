import psycopg2
from config import config


def connect():
    """Connect to the Postgresql database server"""
    conn = None

    try:
        params = config()
        print('Connecting to the Postgresql database....')
        # ** = Apuntando a un diccionario
        conn = psycopg2.connect(**params)

        # create cursor
        cursor = conn.cursor()
        print('Postgresql database version: ')
        cursor.execute('SELECT version()')

        # Display the Postgresql database server version
        db_version = cursor.fetchone()
        print(db_version)

        # close the communication with the Postgresql
        cursor.close()
    except(Exception, psycopg2.DataError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
