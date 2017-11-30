import psycopg2
from config import config

def get_empleado():
    """ query data from the empleado table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT id_empleado, nombre, apellido, nif, seg_social, departamento, puesto FROM empleado ORDER BY nombre")


        print("The number of empleados: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_empleado()

