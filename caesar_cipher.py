def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_caesar(ciphertext):
    print("Brute Force Caesar Decryption:")
    for shift in range(1, 26):
        decrypted_text = ''
        for char in ciphertext:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            else:
                decrypted_text += char
        print(f"Shift {shift:2}: {decrypted_text}")
