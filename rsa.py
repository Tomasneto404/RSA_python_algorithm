from functions import *



while True:
    print("""
RSA Algorithm - Implemented by Tomás Neto in 2024
------------------------------------------------
        1 - Encrypt\n
        2 - Decrypt\n\n
        0 - Quit
------------------------------------------------
        
        """)
    try:
        user_input = int(input("> "))
    except:
        print("ERROR: Invalid value.")
        break

    if user_input == 1:
        
        print("""
RSA Algorithm - Implemented by Tomás Neto in 2024
------------------------------------------------
        1 - Generate cipher\n
        2 - Known public key\n\n
        0 - Back
------------------------------------------------
        """)
        
        try:
            second_user_input = int(input("> "))
        except:
            print("ERROR: Invalid value.")
            break
        
        if second_user_input == 1:
            nbits = int(input("Key size (bits): "))
            m = input("Message to encrypt: ")
            rsa_generate_cipher(m, nbits)
        
        elif second_user_input == 2:
            print("Public key values")
            e = int(input("e: "))
            n = int(input("n: "))
            m = input("Message to encrypt: ")
            rsa_encrypt(e, n, m)
        
    elif user_input == 2:
        print("Private key values")
        n = int(input("n > "))
        d = int(input("d > "))
        c = int(input("c > "))
        rsa_decrypt(n, d, c)
        
    else:
        break
    