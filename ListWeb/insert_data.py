import psycopg2
from config import config


def insert_empleado(nombre, apellido, nif, seg_social, departamento, puesto):
    """ Insert data into the empleado table"""

    sql = """INSERT INTO empleado(nombre, apellido, nif, seg_social, departamento, puesto)
                    VALUES ( %s, %s, %s, %s, %s,%s) RETURNING id_empleado;"""

    connetion = None
    id_empleado = None
    try:
        # read database configuration
        params = config()
        # Connect to the PostgreSQL database
        connetion = psycopg2.connect(**params)
        # create a new cursor
        cursor = connetion.cursor()
        # execute the INSERT statement
        cursor.execute(sql, (nombre, apellido, nif, seg_social, departamento, puesto))
        # get the generated id back
        id_empleado = cursor.fetchone()[0]
        # commint the changes to the database
        connetion.commit()
        # close the communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connetion is not None:
            connetion.close()
    return id_empleado



if __name__ == '__main__':
    # insert one vendor
    insert_empleado('Josefina. ',
                    'sds',
                    'sds',
                    'ff',
                    'hh',
                    'hhh')
    # Insert multiple vendors
