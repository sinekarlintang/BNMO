import csv
import Function

import Parser


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

def login():
    inputUsername = str(input())
    id = Parser.cariID("username", inputUsername)
    if id == "x":
        print("Tidak ada username tersebut")
    else:
        nama = Parser.cari("nama", id)
        print(f"Selamat Datang, {nama}!")

