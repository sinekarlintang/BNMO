def length(x):
    # mirip function len
    count = 0
    for i in x:
        count += 1
    return count

def validasi(masukan, type):
    count = 0
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
    for i in masukan:
        for j in char:
            if i == j:
                count += 1
    if count < length(masukan):
        print(f"{type} hanya boleh mengandung alphabet, angka, '-', dan '_'")
        newinput = str(input(f"Masukkan {type}: "))
        return validasi(newinput, type)
    else:
        return masukan
