from time import localtime, time
from Function import length
from UI import header

#Mencari output LCG (Linear Congruential Generator)
def LCG(Y):
    #Inisialisasi constant dengan menggunakan waktu
    a=localtime().tm_sec**localtime().tm_min
    m=time()

    #Menentukan output LCG
    cng=(a*Y)%m
    return str(int(cng))
header("MAGIC CONCH SHELL")
#Meminta pertanyaan user
Q=input("Silahkan ajukan pertanyaan: ")

#Menjadikan panjang character pertanyaan menjadi seed untuk LCG
num=length(Q)
random_num=LCG(num)
temp=length(random_num)

#Kumpulan jawaban yang mungkin
A=["Iya.", "Tidak.", "Benar.", "Salah.", "Bisa jadi.", "Sepertinya tidak.", "Sebaiknya jangan.", "Entahlah.", "Mungkin.", "*Confused machine sounds*"]

#Menampilkan jawaban berdasarkan digit terakhir output LCG
print()
print(A[int(random_num[temp-1])])