import psycopg2
from config import config


def create_table() -> object:
    """"Create tables in the Postgresql in the Database"""

    commands = ("""CREATE TABLE empleado( id_empleado serial NOT NULL,
                                        nombre character varying(100) NOT NULL,
                                        apellido character varying(100) NOT NULL,
                                        nif character varying(100) NOT NULL,
                                        seg_social character varying(100) NOT NULL,
                                        departamento character varying(100) NOT NULL,
                                        puesto character varying(100) NOT NULL,
                                        CONSTRAINT empleado_pkey PRIMARY KEY (id_empleado ))""",
                )
    connection = None
    try:
        # read the connection parameters.
        params = config()
        # connect to the Postgresql Server
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostegreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_table()
