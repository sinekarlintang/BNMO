from csv_parser import readFile,writeFile,appendMatrix,cari,changevalue,save
from Function import length

def register(folder):
    print("Daftarkan akun Anda")
    userfile = folder[3]
    id = length(userfile)
    nama = str(input())
    username = str(input())
    password = str(input())
    role = "user"
    saldo = 0
    cekUsername = cari(userfile, "username", username, "id")
    if cekUsername == "x":
        folder[3] = appendMatrix(userfile, [str(id),username,nama,password,role,str(saldo)])
        save(folder)
    else:
        print("Username sudah terpakai. Silakan ganti username.")
        register(folder)

def login(folder):
    print("Selamat datang kembali.")
    file = folder[3]
    inputUsername = str(input())
    inputPassword = str(input())
    password = cari(file, "username", inputUsername, "password")
    nama = cari(file, "username", inputUsername, "nama")
    if password == inputPassword:
        print(f"Selamat Datang, {nama}!")
    else:
        print("Password atau username salah atau tidak ditemukan.")
        login(folder)

def gantiPassword():
    file = readFile("user.csv")
    changevalue(file, "password", "3", "143")
    print(file)
    writeFile("user.csv", file, 6)
