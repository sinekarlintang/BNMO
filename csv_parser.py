from Function import length
#Membaca data file dan dirubah menjadi array matriks
# X: nama file csv (str; Ex: "game.csv")
def readFile(X):
    with open(X, "r+") as file1:
        #Inisialisasi
        isi=file1.readlines()
        rows=0
        category=1

        #Menghitung jumlah rows/baris
        for i in isi:
            rows+=1

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
# X: nama file csv (str; Ex: "game.csv");   Y=Data yang ingin dimasukkan (dalam bentuk matriks)
def writeFile(X, Y):
    with open(X, "a+") as file1:
        file1.write("\n")
        category=0
        for i in Y:
            category+=1
        
        for i in range (category):
            file1.write(Y[i])
            if i!=(category-1):
                file1.write(";")

#Mengganti SELURUH data pada file dengan yang baru (Dipakai ketika ingin merubah suatu data yang sudah ada)
# X: nama file csv (str; Ex: "game.csv");   Y=Data yang ingin dimasukkan (dalam bentuk matriks);
# Z=Jumlah kategori (int)
def replaceFile(X, Y, Z):
    #Menghitung jumlah baris
    isi=readFile(X)
    count=0
    for i in isi:
        count+=1

    with open(X, 'w+') as file1:
        for i in range (count):
            for j in range (Z):
                file1.write(Y[i][j])
                if j!=(Z-1):
                    file1.write(";")
            if i!=(count-1):
                file1.write("\n")  

# def cari digunakan untuk mencari elemen pada suatu file csv
# contoh : cari(readFile(user.csv), "id", "3", "username")
# artinya : pada file user.csv, ingin dicari username pengguna dengan id "3"
def cari(file, kategori, cari, hasil):
    kategoriFound = False
    while kategoriFound == False:
        for j in range(length(file[0])):
            if file[0][j] == kategori:
                x = j
                kategoriFound = True
    hasilFound = False
    while hasilFound == False:
        for k in range(length(file[0])):
            if file[0][k] == hasil:
                y = k
                hasilFound = True
    found = False
    for i in range(length(file[0])-2):
        if file[i][x] == cari:
            result = file[i][y]
            found = True
            return result
        elif file[i][x] != cari:
            pass

    if not found:    
        return "x"
    else:
        return result