# hill_cipher.py

import numpy as np

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m using Extended Euclidean Algorithm."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    """Find the inverse of a 2x2 matrix under modulo."""
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible modulo {}".format(modulus))

    # Adjugate matrix for 2x2
    adj = np.array([[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]])
    inv_matrix = (det_inv * adj) % modulus
    return inv_matrix.astype(int)

def clean_text(text):
    """Remove non-alphabet characters and convert to uppercase."""
    return ''.join([c for c in text.upper() if c.isalpha()])

def pad_text(text, block_size):
    """Pad text with 'X' to make its length a multiple of block_size."""
    while len(text) % block_size != 0:
        text += 'X'
    return text

def text_to_numbers(text):
    return [ALPHABET.index(c) for c in text]

def numbers_to_text(numbers):
    return ''.join([ALPHABET[n % 26] for n in numbers])

def hill_encrypt(text, key_matrix):
    block_size = key_matrix.shape[0]
    text = pad_text(clean_text(text), block_size)
    numbers = text_to_numbers(text)
    
    cipher_nums = []
    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i+block_size])
        cipher_block = np.dot(key_matrix, block) % 26
        cipher_nums.extend(cipher_block)
    
    return numbers_to_text(cipher_nums)

def hill_decrypt(cipher_text, key_matrix):
    block_size = key_matrix.shape[0]
    numbers = text_to_numbers(cipher_text)
    inverse_matrix = matrix_mod_inv(key_matrix, 26)
    
    plain_nums = []
    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i+block_size])
        plain_block = np.dot(inverse_matrix, block) % 26
        plain_nums.extend(plain_block)
    
    return numbers_to_text(plain_nums)
