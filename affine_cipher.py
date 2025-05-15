ffrom math import gcd

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a = {a} under mod {m}.")

def is_valid_key(a):
    return gcd(a, 26) == 1

def encrypt_affine(plaintext, a, b):
    if not is_valid_key(a):
        raise ValueError("Key 'a' must be coprime with 26.")
    
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            encrypted = (a * x + b) % 26
            ciphertext += chr(encrypted + base)
        else:
            ciphertext += char
    return ciphertext

def decrypt_affine(ciphertext, a, b):
    if not is_valid_key(a):
        raise ValueError("Key 'a' must be coprime with 26.")
    
    a_inv = mod_inverse(a, 26)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            decrypted = (a_inv * (y - b)) % 26
            plaintext += chr(decrypted + base)
        else:
            plaintext += char
    return plaintext
