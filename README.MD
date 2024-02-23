# Rivest Shamir Adleman algorithm

## Assimetric Encryption/ Decryption system
This program was developed to test my knowledge about the RSA encryption system. It works with the real RSA algorithm.

### Encryption
**METHOD 1 - Traditional encryption with public key**<br>
INPUT: 
       - Public key (_e, n_);<br>
       - Plaintext message (_m_).

OUTPUT: 
       - Ciphertext (_c_).

**METHOD 2 - Generate the whole cipher**<br>
INPUT: 
       - Number of bits that the modulus (_n_) must have;<br>
       - Plaintext message (_m_)

OUTPUT: 
       - Two random prime numbers (_p_ and _q_) that originated _n_ with the provided number of bits;<br>
       - The expoent (_e_) that by default is always 65537;<br>
       - The modular inverse of _e_ (_d_) that verifies the following function: _d_*_e_ ≡ 1 mod ɸ(_n_);<br>
       - _ASCII_ encoded message (_m_);<br>
       - Ciphertext (_c_).

To encrypt a plaintext, the first step is to enconde _m_ with the _ASCII_ codes. In order to simplify the decription, the _ASCII_ codes must have a max length of **two** numbers, it means that the message must be written **only** with the following caracters.

ALLOWED CARACTERS
- letters --> A B C D E F G H I J K L M N O P Q R S T U V W X Y Z and a b c
- numbers --> 0 1 2 3 4 5 6 7 8 9
- special caracters --> (_space_) ! " # $ % & ' ( ) * + , - . / : ; < > = ? @ [ ] \ ^ _ `

ENCRYPTION FORMULA
_c = m^e mod n_, also known as _m^e ≡ c mod n_


### Decryption
**Tradition decryption with private key**
INPUT: Private key (_d_, _n_);
       Ciphertext (_c_).

DECRYPTION FORMULA
_m = c^d mod n_, also known as _c^d ≡ m mod n_
