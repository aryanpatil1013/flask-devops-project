from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'db'),
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'password'),
        database=os.environ.get('MYSQL_DATABASE', 'flaskdb')
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO names (name) VALUES (%s)', (name,))
        conn.commit()
        cursor.close()
        conn.close()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM names')
    names = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
