from caesar_cipher import caesar_encrypt, caesar_decrypt, brute_force_caesar
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

def main():
    print("=== Crypto Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt, (D)ecrypt, (B)rute force (Caesar), or (V)igenère? ").lower()

    if choice in ['e', 'd', 'b']:
        text = input("Enter your message: ")
        shift = int(input("Enter shift number (e.g. 3): "))

        if choice == 'e':
            encrypted = caesar_encrypt(text, shift)
            print("Encrypted message:", encrypted)
        elif choice == 'd':
            decrypted = caesar_decrypt(text, shift)
            print("Decrypted message:", decrypted)
        elif choice == 'b':
            encrypted_message = caesar_encrypt(text, shift)  # Encrypt first for brute-force testing
            print("\n--- Brute Force Results ---")
            brute_force_caesar(encrypted_message)

    elif choice == 'v':
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

    else:
        print("Invalid choice. Please enter E, D, B, or V.")

if __name__ == "__main__":
    main()

