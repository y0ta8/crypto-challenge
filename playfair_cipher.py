def prepare_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))

    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        digraphs.append(a + b)

    return digraphs


def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    seen = set()

    for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None


def encrypt_digraph(pair, matrix):
    a, b = pair
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def decrypt_digraph(pair, matrix):
    a, b = pair
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def encrypt_playfair(plaintext, key):
    digraphs = prepare_text(plaintext)
    matrix = generate_matrix(key)
    return ''.join(encrypt_digraph(pair, matrix) for pair in digraphs)


def decrypt_playfair(ciphertext, key):
    digraphs = prepare_text(ciphertext)
    matrix = generate_matrix(key)
    return ''.join(decrypt_digraph(pair, matrix) for pair in digraphs)
