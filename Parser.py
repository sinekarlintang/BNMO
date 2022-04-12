import csv

def cariID(jenis, cari):
    file = open("user.csv","r+", newline='')
    reader = csv.reader(file, delimiter=";")

    if jenis == "username": x = 1
    elif jenis == "nama": x = 2
    elif jenis == "password": x = 3
    elif jenis == "role": x = 4
    elif jenis == "saldo": x = 5
    
    found = False
    for i in (reader):
        if i[x] == cari:
            id = i[0]
            found = True
            return id
        elif i[x] != cari:
            pass

    if not found:    
        return "x"
    else:
        return id

def cari(jenis,id):
    file = open("user.csv","r+", newline='')
    reader = csv.reader(file, delimiter=";")
    if jenis == "username":
            x = 1
    elif jenis == "nama":
        x = 2
    elif jenis == "password":
        x = 3
    elif jenis == "role":
        x = 4
    elif jenis == "saldo":
        x = 5

    found = False
    for row in reader:
        if row[0] == id:
            hasil = row[x]
            found = True
        else:
            pass
    if not found:    
        return "x"
    else:
        return hasil