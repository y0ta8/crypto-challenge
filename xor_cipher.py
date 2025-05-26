# xor_cipher.py

def xor_encrypt_decrypt(text: str, key: str) -> str:
    """
    Encrypts or decrypts the given text using XOR cipher with the provided key.
    
    Parameters:
    - text: The input string to be encrypted or decrypted.
    - key: The key string used for XOR operation.
    
    Returns:
    - A string that is the result of XORing each character of the input text with the key.
    """
    if not key:
        raise ValueError("Key must not be empty.")

    output = []
    for i in range(len(text)):
        xor_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        output.append(xor_char)

    return ''.join(output)
