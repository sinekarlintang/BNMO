from csv_parser import cari
from Function import length

def header(title):
    print("\n")
    for i in range ((30-length(title)//2)):
        print("=", end="")
    print(f" {title} ", end="")
    for i in range ((30-length(title)//2)):
        print("=", end="")
    print("\n")

def startmenu():
    header("MENU")
    print("Selamat datang di BNMO!")
    print("Commands : \n    register\n    log in\n    exit")

def usermenu(folder,id):
    nama = cari(folder[3], "id", id, "nama")
    header("MAIN MENU")
    print(f"Halo, {nama}!\n")
    print(" __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ____   ____   ___ ___   ___   __ \n|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |    \ |    \ |   |   | /   \ |  |\n|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    |  o  )|  _  || _   _ ||     ||  |\n|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |     ||  |  ||  \_/  ||  O  ||__|\n|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |    |  O  ||  |  ||   |   ||     | __ \n \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |    |     ||  |  ||   |   ||     ||  |\n  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/     |_____||__|__||___|___| \___/ |__|\n                                                                                                              ")
    print("Commands : \n     MagicConchShell\n     TicTacToe\n     buy_game : membeli game baru\n     list_game : melihat game yang dimiliki\n     search_my_game : mencari game yang dimiliki")
    print("     list_game_toko : melihat game di toko\n     search_game_at_store : mencari game di toko\n     riwayat : lihat riwayat pembelian\n     help : bantuan")
    print("     save : simpan data\n     exit : keluar BNMO")

def adminmenu(folder,id):
    nama = cari(folder[3], "id", id, "nama")
    header("MAIN MENU")
    print(f"Halo, {nama}!\n")
    print(" __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ____   ____   ___ ___   ___   __ \n|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |    \ |    \ |   |   | /   \ |  |\n|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    |  o  )|  _  || _   _ ||     ||  |\n|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |     ||  |  ||  \_/  ||  O  ||__|\n|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |    |  O  ||  |  ||   |   ||     | __ \n \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |    |     ||  |  ||   |   ||     ||  |\n  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/     |_____||__|__||___|___| \___/ |__|\n                                                                                                              ")
    print("Commands : \n     tambah_game : tambah game baru\n     ubah_game : mengubah detil game\n     ubah_stok : mengubah stok game")
    print("     list_game_toko : melihat game di toko\n     search_game_at_store : mencari game di toko\n     top_up : top up saldo user\n     help : bantuan")
    print("     save : simpan data\n     exit : keluar BNMO")

