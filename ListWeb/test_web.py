from flask import Flask, render_template, redirect, request
from insert_data import insert_empleado
from use_database import UseDatabase
from delete_empleado import delete_empleado
from update_data import update_empleado

app = Flask(__name__)

"""Directiva"""


@app.route('/')
def home() -> '302':
    return redirect('/entry')


"""Redirege una pagina web como retorno"""


@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido al alta de empleados')


"""Direccion para ocupar en el entry"""
# Create the fed view_log
@app.route('/viewlog')
def view_log() -> 'html':
    contents = []
    with open('vsearchbd.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
                # contents = log.readlines()
        tittles = ('id_empleado', 'nombre', 'apellido', 'nif', 'seg_social', 'departamento', 'puesto')
    return render_template('vsearchbd.html',
                           the_tittle='View Log',
                           the_row_tittles=tittles,
                           the_data=contents)


@app.route('/viewlogdb')
def view_log_db() -> 'html':
    with UseDatabase() as cursor:

        _SQL = """SELECT id_empleado, nombre, apellido, nif, seg_social, departamento, puesto  FROM empleado"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        tittles = ('id_empleado', 'nombre', 'apellido', 'nif', 'seg_social', 'departamento', 'puesto' )
        return render_template('viewlog.html',
                               the_tittle='View Log DB',
                               the_row_tittles=tittles,
                               the_data=contents)

@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    """Valores a recibir en las cajas de texto"""
    Nombre = request.form['nombre']
    Apellido = request.form['apellido']
    Nif = request.form['nif']
    Seg = request.form['seg']
    Departamento = request.form['departamento']
    Puesto = request.form['puesto']

    result = insert_empleado(Nombre, Apellido, Nif, Seg, Departamento, Puesto)

    with UseDatabase() as cursor:
        _SQL = """SELECT id_empleado, nombre, apellido, nif, seg_social, departamento, puesto  FROM empleado"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        tittles = ('id_empleado', 'nombre', 'apellido', 'nif', 'seg_social', 'departamento', 'puesto')
        return render_template('viewlog.html',
                               the_tittle='View Log DB',
                               the_row_tittles=tittles,
                               the_data=contents)




#Eliminar
@app.route('/eliminar', methods=['POST'])
def eliminar() -> 'html':
    id = request.form['eliminar']
    result = delete_empleado(id)
    comen = 'Se elimino exitozamente'


    with UseDatabase() as cursor:
        _SQL = """SELECT id_empleado, nombre, apellido, nif, seg_social, departamento, puesto  FROM empleado"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        tittles = ('id_empleado', 'nombre', 'apellido', 'nif', 'seg_social', 'departamento', 'puesto')
        return render_template('viewlog.html',
                               the_tittle='View Log DB',
                               the_row_tittles=tittles,
                               the_data=contents)


#Actualizar
@app.route('/actualizar', methods=['POST'])
def actualizar() -> 'html':
    idActualizar = request.form['id']
    Nombre = request.form['nombre']
    Apellido = request.form['apellido']
    Nif = request.form['nif']
    Seg = request.form['seg']
    Departamento = request.form['departamento']
    Puesto = request.form['puesto']

    result = update_empleado(idActualizar, Nombre, Apellido, Nif, Seg, Departamento, Puesto)
    with UseDatabase() as cursor:
        _SQL = """SELECT id_empleado, nombre, apellido, nif, seg_social, departamento, puesto  FROM empleado"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        tittles = ('id_empleado', 'nombre', 'apellido', 'nif', 'seg_social', 'departamento', 'puesto')
        return render_template('viewlog.html',
                               the_tittle='View Log DB',
                               the_row_tittles=tittles,
                               the_data=contents)


app.run(debug=True)
