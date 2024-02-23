import random
from sympy import mod_inverse

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def prime_generator(n): 
    while True:
        prime_candidate = random.getrandbits(n)

        prime_candidate |= 1
        if miller_rabin(prime_candidate):
            return prime_candidate
        
def rsa_generate_cipher(m, nbits):
    nbits //= 2
    
    
    ascii_message = ""
    for char in m:
        ascii_message += str(ord(char))

    p = prime_generator(nbits)
    q = prime_generator(nbits)
    n = p * q
    e = 65537
    phin = (p - 1)*(q - 1)
    d = mod_inverse(e, phin)

    c = (int(ascii_message) ** e) % n
    
    print("\np:", p)
    print("\nq:", q)
    print("\nn:", n)
    print("\ne:", e)
    print("\nd:", d)
    print("\nm:", ascii_message)
    print("\nc:", c)
    
def rsa_encrypt(e, n, m):
    ascii_message = ""
    for char in m:
        ascii_message += str(ord(char))
    
    c = (int(ascii_message) ** e) % n
    print("\nc:", c)
    
    
def rsa_decrypt(n, d, c):
    m = pow(c, d, n)
    
    messaToASCIIDecode = str(m)
    
    groups = [messaToASCIIDecode[i:i+2] for i in range(0, len(messaToASCIIDecode), 2)]
    ascii_message = ''.join([chr(int(group)) for group in groups])
    
    print("Message:", ascii_message)