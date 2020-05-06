import sqlite3


def data(file_path):
    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()
    result = cursor.execute("SELECT username, grade FROM submissions WHERE course = 'LSINF1101-PYTHON' ")
    tache = []
    grades = []
    grad = []
    indexe = []
    i = 0
    for row in result:
        tache.append(row[0])
        grades.append(row[1])
        i += 1
        if i == 30:
            break
    k = 0
    for j in grades:
        if j == 0:
            k += 5
            j += 1
            grad.append(k)
        else:
            m = 0
            j += 1
            grad.append(m)
    index = 0
    for i in grad:
        if i != 0:
            indice = 0
            i += 1
            indexe.append(indice)
        else:
            index += 5
            i += 1
            indexe.append(index)



    connection.close()
    return [tache, grad, indexe]
