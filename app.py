from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Variables de conexion de la DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'python_fonasa'
mysql = MySQL(app)

# settings SESSION
app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    return render_template('index.html')

# INICIO DE MODULO ESPECILIDADES
@app.route('/specialty')
def specialty():
    speciality = mysql.connection.cursor()
    speciality.execute('SELECT * FROM specialty')
    data = speciality.fetchall()
    speciality.close()
    return render_template('specialty/index.html', specialties = data)

@app.route('/specialty-add', methods=['POST'])
def specialty_add():
    if request.method == 'POST':
        fullname = request.form['fullname']
        sql = "INSERT INTO specialty (name) VALUES ('"+fullname+"')"
        specialty = mysql.connection.cursor()
        specialty.execute(sql)
        mysql.connection.commit()
        specialty.close()
        flash('La especialidad se ha registrado satisfactoriamente')
        return redirect(url_for('specialty'))

@app.route('/specialty-delete/<string:id>', methods=['POST', 'GET'])
def specialty_delete(id):
    specialty = mysql.connection.cursor()
    specialty.execute('DELETE FROM specialty WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('La especialidad se ha ELIMINADO satisfactoriamente')
    return redirect(url_for('specialty'))

@app.route('/specialty-edit/<id>', methods=['POST', 'GET'])
def specialty_edit(id):
    speciality = mysql.connection.cursor()
    sql = "SELECT * FROM specialty WHERE id="+id
    print(sql)
    speciality.execute(sql)
    data = speciality.fetchall()
    print(data)
    speciality.close()
    return render_template('specialty/edit.html', specialty = data[0])

@app.route('/specialty-update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        sql ="UPDATE specialty SET name ='"+fullname+"' WHERE id="+id
        contact = mysql.connection.cursor()
        contact.execute(sql)
        mysql.connection.commit()
        flash('La especialidad se ha ACTUATUALIZADO satisfactoriamente')
        return redirect(url_for('specialty'))
# FIN DE MODULO ESPECILIDADES

if __name__ == '__main__':
    app.run(port = 3000, debug = True)