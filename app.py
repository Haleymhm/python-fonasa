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
    return "<h2> Prueba Técnica <strong> Python - Flask </strong> </h2>"



if __name__ == '__main__':
    app.run(port = 3000, debug = True)