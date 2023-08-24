from flask import Flask, render_template, jsonify, request, redirect
from flask.helpers import url_for
#mport requests
import json
import psycopg2
#import os
from logging import FileHandler,WARNING

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

def get_db_connection():
    conn = psycopg2.connect(database= 'help_desk',
                            user='postgres',
                            password ='root',
                            host= 'localhost')
    
    return conn

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/empleados', methods=['GET'])
def empleados():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from empleados;')
    empleados = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('empleados.html', empleados=empleados)

if __name__ == '__main__':
    app.run()