from caesar_cipher import caesar_encrypt, caesar_decrypt, brute_force_caesar
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from base64_cipher import base64_encode, base64_decode
from transposition import encrypt_columnar_transposition, decrypt_columnar_transposition  # ✅ NEW

def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + 13) % 26 + base)
        else:
            result += char
    return result

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(base + (25 - (ord(char) - base)))
        else:
            result += char
    return result

def show_help():
    print("\n🔐 Crypto Challenge - Help Menu")
    print("Available Options:")
    print("  E    - Encrypt using Caesar Cipher")
    print("  D    - Decrypt using Caesar Cipher")
    print("  B    - Brute-force Caesar Cipher")
    print("  V    - Use Vigenère Cipher (encrypt/decrypt)")
    print("  B64  - Base64 Encoding/Decoding")
    print("  R13  - ROT13 Cipher (symmetric)")
    print("  ATB  - Atbash Cipher (symmetric)")
    print("  T    - Transposition Cipher (encrypt/decrypt)")  # ✅ NEW
    print("  HELP - Show this help menu")
    print("  EXIT - Quit the tool\n")

def main():
    print("=== Crypto Cipher Tool ===")
    show_help()

    while True:
        choice = input("Choose an option (E, D, B, V, B64, R13, ATB, T, HELP, EXIT): ").lower()

        if choice == 'exit':
            print("👋 Goodbye!")
            break
        elif choice == 'help':
            show_help()
        elif choice in ['e', 'd', 'b']:  # Caesar Cipher Section
            text = input("Enter your message: ")

            if choice in ['e', 'd']:  # Encryption/Decryption
                shift = int(input("Enter shift number (e.g. 3): "))
                if choice == 'e':
                    encrypted = caesar_encrypt(text, shift)
                    print("Encrypted message:", encrypted)
                elif choice == 'd':
                    decrypted = caesar_decrypt(text, shift)
                    print("Decrypted message:", decrypted)

            elif choice == 'b':  # Brute Force Caesar
                shift = int(input("Enter shift number (e.g. 3): "))
                encrypted_message = caesar_encrypt(text, shift)
                print("\n--- Brute Force Results ---")
                brute_force_caesar(encrypted_message)

        elif choice == 'v':  # Vigenère Cipher Section
            action = input("Encrypt or Decrypt with Vigenère? (E/D): ").lower()
            text = input("Enter your message: ")
            key = input("Enter your key (letters only): ")

            if action == 'e':
                encrypted = vigenere_encrypt(text, key)
                print("Encrypted message:", encrypted)
            elif action == 'd':
                decrypted = vigenere_decrypt(text, key)
                print("Decrypted message:", decrypted)
            else:
                print("Invalid Vigenère action. Use E or D.")

        elif choice == 'b64':  # Base64 Encoding/Decoding Section
            action = input("Do you want to (E)ncode or (D)ecode Base64? ").lower()
            text = input("Enter your message: ")

            if action == 'e':
                encoded = base64_encode(text)
                print("Encoded Base64 message:", encoded)
            elif action == 'd':
                decoded = base64_decode(text)
                print("Decoded message:", decoded)
            else:
                print("Invalid action. Use E or D for Base64.")

        elif choice == 'r13':
            text = input("Enter your message: ")
            result = rot13(text)
            print("ROT13 result:", result)

        elif choice == 'atb':
            text = input("Enter your message: ")
            result = atbash_cipher(text)
            print("Atbash result:", result)

        elif choice == 't':  # ✅ NEW: Transposition Cipher
            action = input("Encrypt or Decrypt with Transposition? (E/D): ").lower()
            text = input("Enter your message: ")
            keyword = input("Enter your keyword: ")

            if action == 'e':
                encrypted = encrypt_columnar_transposition(text, keyword)
                print("Encrypted message:", encrypted)
            elif action == 'd':
                decrypted = decrypt_columnar_transposition(text, keyword)
                print("Decrypted message:", decrypted)
            else:
                print("Invalid action. Use E or D for Transposition.")

        else:
            print("❌ Invalid choice. Type 'help' to see available options.")

if __name__ == "__main__":
    main()
