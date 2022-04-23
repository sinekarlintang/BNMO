a = 3
b = 5
m = 95

def affine(a,b,m,x):
    z = ord(x)-31
    y = ((z*a + b) % m)+31
    return chr(y)

def unaffine(a,b,m,x):
    z = ord(x)-31
    y = ((modInverse(a,m) * (z - b)) % m)+31
    return chr(y)

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

def encrypt(password):
    input = str(password)
    encrypted = ""
    for char in input:
        encrypted += affine(a,b,m,char)
    return encrypted

def decrypt(password):
    input = str(password)
    decrypted = ""
    for char in input:
        decrypted += unaffine(a,b,m,char)
    return decrypted

print(decrypt("!"))
print(encrypt("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"))