from csv_parser import readFile,writeFile,appendMatrix,cari,changevalue
from Function import length

def register():
    print("Daftarkan akun Anda")
    file = readFile("user.csv")
    id = length(file)
    nama = str(input())
    username = str(input())
    password = str(input())
    role = "user"
    saldo = 0
    cekUsername = cari(file, "username", username, "id")
    if cekUsername == "x":
        newfile = appendMatrix(file, [str(id),username,nama,password,role,str(saldo)])
        simpan = save("user.csv", newfile, 6)
        if simpan == "saved":
            print(f"Selamat Datang, {nama}!")
        elif simpan == "not saved":
            register()
    else:
        print("Username sudah terpakai. Silakan ganti username.")
        register()

def login():
    print("Selamat datang kembali.")
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

def gantiPassword():
    file = readFile("user.csv")
    changevalue(file, "password", "3", "143")
    print(file)
    writeFile("user.csv", file, 6)

def save(file, data, intkategori):
    choice = input("Apakah perubahan ingin disimpan? (Y/N) : ")
    if choice == "Y":
        writeFile(file, data, intkategori)
        print("Perubahan berhasil disimpan.")
        return "saved"
    elif choice == "N":
        print("Perubahan tak disimpan.")
        return "not saved"
    else:
        print("Invalid input!")
        save(file, data, intkategori)
