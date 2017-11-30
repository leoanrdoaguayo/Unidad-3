import psycopg2
from config import config


def seleciconar_empleado(id_empleado):
    """ update vendor name based on the vendor id"""
    sql = """SELECT  nombre, apellido, nif, seg_social, departamento, puesto  FROM empleado WHERE id_empleado = %s"""

    try:
        connection = None
        updated_rows = 0

        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(sql, (id_empleado))

        updated_rows = cursor.rowcount

        connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return updated_rows


if __name__ == '__main__':
   seleciconar_empleado(4)
