import psycopg2
from config import config
"""Name:Leonardo Israel Aguayo González"""

def write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    conn = None
    try:
        # read data from a picture
        drawing = open(path_to_file, 'rb').read()
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO part_drawings(part_id, file_extension, drawing_data)"
                    + "VALUES (%s, %s, %s)", (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    write_blob(7, 'images/jaguar-f-type-v6-s-review-2013_59.jpg', 'jpg')
    write_blob(8, 'images/simtray.jpg', 'jpg')


