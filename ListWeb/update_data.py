import psycopg2
from config import config


def update_empleado(id_empleado,nombre, apellido, nif, seg_social, departamento, puesto):
    """ update vendor name based on the vendor id"""
    sql = """ UPDATE empleado SET nombre = %s, apellido = %s, nif = %s,
                    seg_social = %s, departamento = %s, puesto = %s WHERE id_empleado = %s"""

    try:
        connection = None
        updated_rows = 0

        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(sql, (nombre, apellido, nif, seg_social, departamento, puesto,  id_empleado))

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
    update_empleado(5, '3M Corpwdfdddddddddddddddddddddddscdd.',
                        '1',
                        '2',
                        '3',
                        '4',
                     '5')
