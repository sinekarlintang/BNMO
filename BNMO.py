import argparse
from Commands import register,login
import os
from csv_parser import readFile
from Function import length

def main(matrix):

    print("Selamat datang di BNMO!")
    choice = str(input("Masukkan perintah! : "))
    if choice == "register":
        register(matrix)
        main(matrix)
    elif choice == "log in":
        login(matrix)
        main(matrix)
    elif choice == "exit":
        print("Sampai jumpa lagi!")
        exit()
    
loaded = False
parser = argparse.ArgumentParser()
parser.add_argument('foldername', type=str)
args = parser.parse_args()
for (root,dirs,files) in os.walk(args.foldername, topdown=True):
    matrix = [0 for j in range (length(files))]
    for i in range (length(files)):
        matrix[i] = readFile(f"{args.foldername}/{files[i]}")
    loaded = True

if loaded :
    main(matrix)
else :
    print("Nama folder tidak ditemukan")