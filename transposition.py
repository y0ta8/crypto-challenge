def encrypt_columnar_transposition(plaintext: str, keyword: str) -> str:
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()

    key_order = sorted(list(keyword))
    num_cols = len(keyword)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    padded_len = num_rows * num_cols
    plaintext += 'X' * (padded_len - len(plaintext))

    matrix = ['' for _ in range(num_cols)]
    for idx, char in enumerate(plaintext):
        col = idx % num_cols
        matrix[col] += char

    sorted_matrix = [x for _, x in sorted(zip(keyword, matrix))]

    return ''.join(sorted_matrix)


def decrypt_columnar_transposition(ciphertext: str, keyword: str) -> str:
    keyword = keyword.upper()
    num_cols = len(keyword)
    num_rows = len(ciphertext) // num_cols

    key_order = sorted([(char, i) for i, char in enumerate(keyword)])
    indices = [index for _, index in key_order]

    chunks = [ciphertext[i * num_rows:(i + 1) * num_rows] for i in range(num_cols)]

    original_order = [''] * num_cols
    for idx, original_idx in enumerate(indices):
        original_order[original_idx] = chunks[idx]

    plaintext = ''
    for row in range(num_rows):
        for col in range(num_cols):
            plaintext += original_order[col][row]

    return plaintext.rstrip('X')
