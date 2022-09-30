from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import hashlib

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

@app.before_request
def protected_request():
    ruta = request.path
    if not 'loggedin' in session:
        if ruta != "/login" and ruta != "/hacer_login" and ruta != "/logout" and not ruta.startswith("/static"):
            flash('Debe iniciar sision')
            return render_template('login.html')


@app.route('/') 
@app.route('/login', methods =['GET', 'POST']) 
def login(): 
    if request.method == 'POST': 
        username = request.form['email'] 
        password = request.form['password']
        result = hashlib.md5(password.encode())
        pass_has = result.hexdigest()
        sql = "SELECT * FROM users WHERE email='"+username+"' AND password='"+pass_has+"'"
        user = mysql.connection.cursor()
        user.execute(sql)
        data = user.fetchall()
        account = data
        user.close()

        if account :
            userlog = data[0]
            session['loggedin'] = True
            session['id'] = userlog[0]
            session['fullname'] = userlog[1]
            print(userlog[1])
            return redirect(url_for('Home'))
        else:
            flash('Error usuario y/o contraseña')

    return render_template('login.html')

@app.route('/logout')
def Logout():
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('fullname', None) 
    return redirect(url_for('login'))

@app.route('/home')
def Home():
    
    #print(username)
    return render_template('home.html', username = session['fullname'])

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

# INICIO DE MODULO ESPECAILISTA
@app.route('/specialist')
def specialist():
    specialists = mysql.connection.cursor()
    specialists.execute('SELECT specialist.id, specialist.fullname, specialty.name  FROM specialist, specialty WHERE specialty.id = specialist.specialty_id')
    data = specialists.fetchall()
    specialists.close()
    speciality = mysql.connection.cursor()
    speciality.execute('SELECT * FROM specialty')
    data1 = speciality.fetchall()
    return render_template('specialist/index.html', specialists = data, specialties = data1)

@app.route('/specialist-add', methods=['POST'])
def add_specialist():
    if request.method == 'POST':
        fullname = request.form['fullname']
        specialty_id = request.form['specialtyid']

        specialist = mysql.connection.cursor()
        sql = "INSERT INTO specialist (fullname, specialty_id) VALUES ('"+fullname+"','"+specialty_id+"')"
        
        specialist.execute(sql)
        mysql.connection.commit()
        specialist.close()
        flash('EL Registro se ha registrado satisfactoriamente')
        return redirect(url_for('specialist'))

@app.route('/specialist-delete/<string:id>', methods=['POST', 'GET'])
def specialist_delete(id):
    specialist = mysql.connection.cursor()
    specialist.execute('DELETE FROM specialist WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El registro se ha ELIMINADO satisfactoriamente')
    return redirect(url_for('specialist'))

@app.route('/specialist-edit/<id>', methods=['POST', 'GET'])
def specialist_edit(id):
    speciality = mysql.connection.cursor()
    sql = "SELECT * FROM specialist WHERE id="+id
    speciality.execute(sql)
    data = speciality.fetchall()
    speciality.close()

    speciality = mysql.connection.cursor()
    speciality.execute('SELECT * FROM specialty')
    data1 = speciality.fetchall()
    speciality.close()
    
    return render_template('specialist/edit.html', specialist = data[0], specialties = data1)

@app.route('/specialist-update/<id>', methods=['POST', 'GET'])
def specialist_update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        specialty_id = request.form['specialtyid']
        speciality = mysql.connection.cursor()
        sql ="UPDATE specialist SET fullname ='"+fullname+"', specialty_id='"+specialty_id+"' WHERE id="+id
        speciality.execute(sql)
        mysql.connection.commit()
        speciality.close()
        flash('EL Registro se ha actualizado satisfactoriamente')
        return redirect(url_for('specialist'))
# FIN DE MODULO ESPECIALISTA 

# INICIO DE MODULO ESPECAILISTA
@app.route('/institution')
def institution():
    institution = mysql.connection.cursor()
    institution.execute('SELECT institution.id, institution.name, comunas.comuna FROM institution, comunas WHERE institution.comuna_id = comunas.id')
    data = institution.fetchall()
    institution.close()
    comuna = mysql.connection.cursor()
    comuna.execute('SELECT * FROM comunas')
    data1 = comuna.fetchall()
    comuna.close()
    return render_template('institution/index.html', institutions = data, comunas = data1) 

@app.route('/institution-add', methods=['POST'])
def institution_add():
    if request.method == 'POST':
        fullname = request.form['fullname']
        comuna_id = request.form['comuna_id']
        direction = request.form['direction']

        institution = mysql.connection.cursor()
        sql = "INSERT INTO institution (name, direction ,comuna_id) VALUES ('"+fullname+"','"+direction+"', '"+comuna_id+"')"
        
        institution.execute(sql)
        mysql.connection.commit()
        institution.close()
        flash('EL Registro se ha registrado satisfactoriamente')
        return redirect(url_for('institution'))

@app.route('/institution-delete/<string:id>', methods=['POST', 'GET'])
def institution_delete(id):
    institution = mysql.connection.cursor()
    institution.execute('DELETE FROM institution WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El registro se ha ELIMINADO satisfactoriamente')
    return redirect(url_for('institution'))

@app.route('/institution-edit/<id>', methods=['POST', 'GET'])
def institution_edit(id):
    institution = mysql.connection.cursor()
    sql = "SELECT * FROM institution WHERE id="+id
    institution.execute(sql)
    data = institution.fetchall()
    institution.close()

    comuna = mysql.connection.cursor()
    comuna.execute('SELECT * FROM comunas')
    data1 = comuna.fetchall()
    comuna.close()
    
    return render_template('institution/edit.html', institution = data[0], comunas = data1)

@app.route('/institution-update/<id>', methods=['POST', 'GET'])
def institution_update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        comuna_id = request.form['comuna_id']
        direction = request.form['direction']
        institution = mysql.connection.cursor()
        sql ="UPDATE institution SET name ='"+fullname+"', direction='"+direction+"', comuna_id='"+comuna_id+"' WHERE id="+id
        institution.execute(sql)
        mysql.connection.commit()
        institution.close()
        flash('EL Registro se ha actualizado satisfactoriamente')
        return redirect(url_for('institution'))
# INICIO DE MODULO CENTRO MEDICO

# INICIO DE MODULO PACIENTES
@app.route('/patient')
def patient():
    patient = mysql.connection.cursor()
    patient.execute('SELECT * FROM patients')
    data = patient.fetchall()
    patient.close()
    return render_template('patient/index.html', patients = data) 

@app.route('/patient-add', methods=['POST'])
def patient_add():
    if request.method == 'POST':
        rut = request.form['rut']
        fullname = request.form['fullname']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        smoker = request.form['smoker']
        smoker_time = request.form['smoker-time']
        diet = request.form['diet']

        patient = mysql.connection.cursor()
        sql = "INSERT INTO patients (rut, fullname, age ,height, weight,smoker, smoker_time, diet) VALUES ('"+rut+"','"+fullname+"','"+age+"', '"+height+"','"+weight+"','"+smoker+"','"+smoker_time+"','"+diet+"')"
        
        patient.execute(sql)
        mysql.connection.commit()
        patient.close()
        flash('EL Registro se ha registrado satisfactoriamente')
        return redirect(url_for('patient'))

@app.route('/patient-delete/<string:id>', methods=['POST', 'GET'])
def patient_delete(id):
    patient = mysql.connection.cursor()
    patient.execute('DELETE FROM patients WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('El registro se ha ELIMINADO satisfactoriamente')
    return redirect(url_for('patient'))

@app.route('/patient-edit/<id>', methods=['POST', 'GET'])
def patient_edit(id):
    patient = mysql.connection.cursor()
    sql = "SELECT * FROM patients WHERE id="+id
    patient.execute(sql)
    data = patient.fetchall()
    patient.close()
    return render_template('pacient/edit.html', patient = data[0])

@app.route('/patient-update/<id>', methods=['POST'])
def patient_update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        smoker = request.form['smoker']
        smoker_time = request.form['smoker-time']
        diet = request.form['diet']
        patient = mysql.connection.cursor()
        sql = "UPDATE  patients SET  fullname='"+fullname+"', age='"+age+"', height='"+height+"', weight='"+weight+"', smoker='"+smoker+"', smoker_time='"+smoker_time+"', diet='"+diet+"' WHERE id='"+id+"'"
        
        patient.execute(sql)
        mysql.connection.commit()
        patient.close()
        flash('EL Registro se ha registrado satisfactoriamente')
        return redirect(url_for('patient'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)