from csv_parser import readFile,writeFile,cari
from Function import length

def register():
    file = readFile("user.csv")
    id = length(file)
    nama = str(input())
    username = str(input())
    password = str(input())
    role = "user"
    saldo = 0
    cekUsername = cari(file, "username", username, "id")
    if cekUsername == "x":
        writeFile("user.csv", [str(id),username,nama,password,role,str(saldo)])
    else:
        print("Username sudah terpakai. Silakan ganti username.")
        register()

def login():
    inputUsername = str(input())
    inputPassword = str(input())
    file = readFile("user.csv")
    password = cari(file, "username", inputUsername, "password")
    nama = cari(file, "username", inputUsername, "nama")
    if password == inputPassword:
        print(f"Selamat Datang, {nama}!")
    else:
        print("Password atau username salah atau tidak ditemukan.")
        login()