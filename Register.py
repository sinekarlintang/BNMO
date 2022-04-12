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
    writeFile("user.csv", [id,username,nama,password,role,saldo])
    # ini masi error : "write() argument must be str, not int"

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