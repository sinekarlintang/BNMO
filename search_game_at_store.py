from Function import length
from history import limitCharacters

#####################################################################################################

# PROGRAM UTAMA 
# F11
def search_game_at_store(folder) :
# prosedur ini berfungsi untuk mencari game dengan kriteria tertentu di toko
    game = folder[0]
    # inisiasi input 
    game_id = input("Masukkan ID Game: ")
    nama_game = input("Masukkan Nama Game: ")
    harga_game = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print()
    
    # semua input valid/terdefinisi
    array = [game_id,nama_game,kategori,tahun_rilis,harga_game] # agar urutannya sama dengan array game.csv
    valid = [True,True,True,True,True]
    
    # cek apakah ada element kosong atau tidak
    for i in range (length(array)) :
        if array[i] == "" : # jika element kosong akan ditetapkan sebagai False
            valid[i] = False
    
    # jika semua input kosong ("") atau tidak ada masukan sama sekali 
    if valid[0] == False and valid[1] == False and valid[2] == False and valid[3] == False and valid[4] == False : # semua input tidak valid/tidak terdefinisi
        print("Daftar game pada toko yang memenuhi kriteria:")
        i = 0
        j = 0
        while i < (length(game)) : # proses pengecekan dan output
            while j < length(game) :
                print(f"{j+1}. {limitCharacters(game[i][0],7)} | {limitCharacters(game[i][1],20)} | {limitCharacters(game[i][2],12)} | {limitCharacters(game[i][3],7)} | {limitCharacters(game[i][4],7)}")
                j += 1
                i += 1
                break
            
    else : # minimal satu input valid/terdefinisi (bukan "")
        print("Daftar game pada toko yang memenuhi kriteria:")
        k = 0
        for i in (game) :
            ada = True 
            for j in range(length(array)) :
                if i[j] != array[j] and (valid[j] == True):
                    ada = False
                elif not ada :
                    break
            if ada :
                while (k < length(game)) :
                    print(f"{k+1}. {limitCharacters(i[0],7)} | {limitCharacters(i[1],15)} | {limitCharacters(i[2],12)} | {limitCharacters(i[3],7)} | {limitCharacters(i[4],7)}")
                    k += 1
                    break
        if k == 0 : 
            print("Tidak ada game yang memenuhi kriteria")
