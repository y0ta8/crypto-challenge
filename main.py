from caesar_cipher import caesar_encrypt, caesar_decrypt, brute_force_caesar
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from base64_cipher import base64_encode, base64_decode

def main():
    print("=== Crypto Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt, (D)ecrypt, (B)rute force (Caesar), (V)igenère, or (B64) Base64? ").lower()

    if choice in ['e', 'd', 'b']:  # Caesar Cipher Section
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
            encrypted_message = caesar_encrypt(text, shift)  # Encrypt first for brute-force testing
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

    else:
        print("Invalid choice. Please enter E, D, B, V, or B64.")

if __name__ == "__main__":
    main()


