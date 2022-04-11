import csv
import Function



def register():
    file = open("user.csv","r+", newline='')
    userWrite = csv.writer(file, delimiter=";")

    id = Function.length(file)
    nama = input()
    username = input()
    password = input()
    role = "user"
    saldo = 0

    userWrite.writerow([id,username,nama,password,role,saldo])
