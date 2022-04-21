def cipher(x):
    a = 3
    b = 5
    
    y = (ord(x)*a + b) % 64
    return y

def decrypt(x):
    y = (modInverse(3,64) * (x - 5)) % 64
    print(y)

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            print(x)
            return x
    return -1
 
 
# Driver Code
a = 3
m = 64

# Function call
print(cipher("a"))
decrypt(cipher("a"))