import os
import sqlite3

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    data = data_treatment('inginious.sqlite')
    return render_template('index.html', noms = data[0], notes = data[1])

@app.route('/page2')
def p2():
    return render_template('p2.html')

if __name__ == '__main__':
    app.run(debug = True)

def data_treatment(file_path):
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    selction = cur.execute("SELECT username, grade FROM submissions WHERE course = 'LSINF1252'")
    names = []
    grades = []
    i = 0
    for row in selction:
        names.append(row[0])
        grades.append(row[1])
        i+=1
        if i == 10:
            break
    conn.close()
    return [names, grades]

def data_test(file_path):
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    available_table = cur.fetchall()
    conn.close()
    print(available_table)