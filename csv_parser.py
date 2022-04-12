from Function import length

#Membaca data file dan dirubah menjadi array matriks 2D
# X: Nama file csv (str; File harus ada; Ex: "game.csv")
def readFile(X):
    with open(X, "r+") as file1:
        #Inisialisasi
        isi=file1.readlines()
        category=1

        #Menghitung jumlah rows/baris
        rows=length(isi)

        #Menghitung jumlah karakter tiap baris
        size=[-1 for i in range (rows)]
        for i in range (rows):
            for j in isi[i]:
                size[i]+=1
            if i==(rows-1):
                size[i]+=1

        #Menghitung jumlah kategori
        for i in range (size[0]):
            if ((isi[0])[i])==";":
                category+=1
        
        #Memisah setiap kategori pada tiap baris
        for x in range (rows):
            Temp=["" for i in range (category)]
            baris=isi[x]
            for i in range (category):
                if i==0:
                    j=0
                else:
                    j+=1
                while j < size[x]:
                    if baris[j]==";":
                        break
                    Temp[i]+=baris[j]
                    j+=1
            isi[x]=Temp
    return isi

#Menambah atau meng-append data baru ke file dan dirubah dari bentuk matriks menjadi semicolon-seperated-value
# X: Nama file csv (str; File harus ada; Ex: "game.csv");   Y=Data yang ingin dimasukkan (dalam bentuk array 1D)
def appendFile(X, Y):
    with open(X, "a+") as file1:
        file1.write("\n")
        category=length(Y)
        
        for i in range (category):
            file1.write(Y[i])
            if i!=(category-1):
                file1.write(";")

#Mengganti SELURUH data/meng-overwrite data pada file dengan yang baru JIKA FILE SUDAH ADA (Dipakai ketika ingin merubah suatu data yang sudah ada)
#Membuat file baru berisi data JIKA FILE TIDAK ADA
def writeFile(X, Y, Z): # X: Nama file csv (str; File boleh ada dan tidak; Ex: "game.csv");Y=Data yang ingin dimasukkan (Harus dalam bentuk matriks 2D); Z=Jumlah kategori (int)
    #Menghitung jumlah baris
    count=length(Y)

    with open(X, 'w+') as file1:
        for i in range (count):
            for j in range (Z):
                file1.write(Y[i][j])
                if j!=(Z-1):
                    file1.write(";")
            if i!=(count-1):
                file1.write("\n")