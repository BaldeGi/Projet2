import os
import sqlite3

from flask import Flask, render_template


app = Flask(__name__)

#page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

#1ere page
@app.route('/page1')
def p1():
    data = data_treatment('inginious.sqlite') #recupere les donnees
    return render_template('p1.html', noms = data[0], notes = data[1])

#2eme page
@app.route('/page2')
def p2():
    data2 = data_treat('inginious.sqlite')#recupere les donnees
    return render_template('p2.html', tasks = data2[0], succ = data2[1], soum = data2[2])

#3eme page
@app.route('/page3')
def p3():
    data3 = data_t('inginious.sqlite')#recupere les donnees
    return render_template('p3.html', tasks = data3[0], notes = data3[1])

if __name__ == '__main__':
    app.run(debug = True)

def data_treatment(file_path):
    """
    @pre file_path chemin vers la base de donné inginious.sqlite
    @post renvoye un tableau avec les cours et le nombre de soumissions réussies correspondant
    """
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    selction = cur.execute("SELECT DISTINCT course FROM submissions") #prend tout les cours dans la base de donné
    names = []
    for i in selction:
        names.append(i[0])
    succ = []
    #pour chaque cours prends le nombre de soumissions réussi et l'ajoute a succ
    for i in names:
        cur.execute("SELECT task FROM submissions WHERE result = 'success' AND course = '{}'".format(i))
        succ.append(len(cur.fetchall()))
    conn.close()
    return [names, succ]

def data_treat(file_path):
    """
    @pre file_path chemin vers la base de donné inginious.sqlite
    @post renvoye le nom de toutes les taches, le nombre d'essaye, le nombre de réussites pour le cour LSINF1101-PYTHON
    """
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    selection = cur.execute("SELECT DISTINCT task FROM submissions WHERE course ='LSINF1101-PYTHON'") #prend les taches
    tasks = []
    for i in selection:
        tasks.append(i[0])
    success_nbr = []
    for i in tasks:
        cur.execute("SELECT count(*) FROM submissions WHERE course ='LSINF1101-PYTHON' AND result = 'success' AND task = '{}'".format(i)) #prend le nombre de tache réussies
        success_nbr.append(cur.fetchall()[0][0])
    soumissions = []
    for i in tasks:
        cur.execute("SELECT count(*) FROM submissions WHERE course ='LSINF1101-PYTHON' AND task = '{}'".format(i)) #prend le nombre d'essais
        soumissions.append(cur.fetchall()[0][0])
    conn.close()
    return [tasks, success_nbr,soumissions]

def data_t(file_path):
    """
    @pre file_path chemin vers la base de donné inginious.sqlite
    @post renvoye le nom de toutes les taches et leur note moyenne pour le cours LEPL1402 
    """
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()
    selection = cur.execute("SELECT DISTINCT task FROM user_tasks WHERE course = 'LEPL1402'")#prend les taches
    tasks = []
    for i in selection:
        tasks.append(i[0])
    notes = []
    for i in tasks:
        cur.execute("SELECT avg(grade) FROM user_tasks WHERE course = 'LEPL1402' AND task = '{}'".format(i))#prend la note moyen pour chaque tache
        notes.append(cur.fetchall()[0][0])
    conn.close()
    return [tasks, notes]