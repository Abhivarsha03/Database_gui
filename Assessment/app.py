from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database= "postgres", user= "postgres",password= "imabhildi03",host= 'localhost',port="5432")
    return conn

@app.route('/')
def home():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses ORDER BY id")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', data=data)

@app.route('/create')
def add():
    return render_template('add.html')

@app.route('/create',methods=['POST'])
def create():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    cur.execute("INSERT INTO courses (name,fees,duration) VALUES (%s,%s,%s)",(name,fees,duration))
    conn.commit()
    cur.close()
    conn.close()
    return render_template('add.html')

@app.route('/edit', methods=['GET'])
def edit():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses ORDER BY id")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('edit.html', data=data)


@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    cur.execute("UPDATE courses SET name=%s, fees=%s, duration=%s WHERE id=%s", (name, fees, duration, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('edit'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    cur.execute("DELETE FROM courses WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('edit'))

if __name__ == '__main__':
    app.run(debug=True)


