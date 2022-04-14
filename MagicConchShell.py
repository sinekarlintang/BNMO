from time import localtime, time
from Function import length

#Mencaru output LCG (Linear Congruential Generator)
def LCG(Y):
    a=localtime().tm_sec**localtime().tm_min
    m=time()

    cng=(a*Y)%m
    return str(int(cng))

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