from csv_parser import appendMatrix,cari,save
from Function import length, validasi
from Cipher import encrypt, decrypt

def register(folder):
    print("Daftarkan akun Anda")
    userfile = folder[3]
    id = length(userfile)
    nama = str(input("Masukkan nama : "))

    uname = str(input("Masukkan username : "))
    username = validasi(uname, "username")

    password0 = str(input("Masukkan password : "))
    password = validasi(password0, "password")
    
    encrypted = encrypt(password)
    role = "user"
    saldo = 1000000
    cekUsername = cari(userfile, "username", username, "id")
    if cekUsername == "x":
        folder[3] = appendMatrix(userfile, [str(id),username,nama,encrypted,role,str(saldo)])
        save(folder)
    else:
        print("Username sudah terpakai. Silakan ganti username.")
        register(folder)

def login(folder):
    print("Selamat datang kembali.")
    file = folder[3]
    inputUsername = str(input("Masukkan username : "))
    inputPassword = str(input("Masukkan password : "))
    password = cari(file, "username", inputUsername, "password")
    decrypted = decrypt(password)
    id = cari(file, "username", inputUsername, "id")
    if decrypted == inputPassword:
        return id
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return login(folder)


"""def gantiPassword():
    file = readFile("user.csv")
    changevalue(file, "password", "3", "143")
    print(file)
    writeFile("user.csv", file, 6)"""
