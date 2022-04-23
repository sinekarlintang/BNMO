from csv_parser import appendMatrix,cari,save
from Function import length, validasi
from Cipher import encrypt, decrypt

def register(folder):
    print("\nDaftarkan akun Anda")
    userfile = folder[3]
    id = length(userfile)
    name = str(input("\nMasukkan nama : "))
    nama = validasi(name, "nama")

    uname = str(input("\nMasukkan username : "))
    username = validasi(uname, "username")

    password0 = str(input("\nMasukkan password : "))
    password = validasi(password0, "password")
    
    encrypted = encrypt(password)
    role = "user"
    saldo = 1000000
    cekUsername = cari(userfile, "username", username, "id")
    if cekUsername == "x":
        folder[3] = appendMatrix(userfile, [str(id),username,nama,encrypted,role,str(saldo)])
        save(folder)
    else:
        print("\nUsername sudah terpakai. Silakan ganti username.")
        register(folder)

def login(folder):
    print("\nSelamat datang kembali.")
    file = folder[3]
    inputUsername = str(input("\nMasukkan username : "))
    inputPassword = str(input("\nMasukkan password : "))
    password = cari(file, "username", inputUsername, "password")
    decrypted = decrypt(password)
    id = cari(file, "username", inputUsername, "id")
    if decrypted == inputPassword:
        return id
    else:
        print("\nPassword atau username salah atau tidak ditemukan.")
        return login(folder)
