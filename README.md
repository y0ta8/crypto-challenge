# Crypto Challenge

This project is focused on building an encryption and decryption tool using different cryptographic algorithms. Every day, a new concept or feature will be implemented and added to the tool.

## 30-Day Plan

### ✅ Day 1: Caesar Cipher
- Implemented Caesar Cipher encryption and decryption
- Added brute-force decryption
- Integrated Caesar Cipher into the CLI tool

### ✅ Day 2: Vigenère Cipher
- Implemented Vigenère Cipher encryption and decryption
- Updated `main.py` to support Vigenère Cipher interaction

### ✅ Day 3: Base64 Encoding/Decoding
- Implemented Base64 encoding and decoding functionality using Python's `base64` module
- Added encode and decode functions to the CLI tool

### ✅ Day 4: Unit Testing & Validation
- Implemented unit tests for **Caesar Cipher**, **Vigenère Cipher**, and **Base64 Encoding/Decoding**
- Ensured all algorithms are thoroughly tested for correctness and edge cases

### ✅ Day 5: Help Menu & CLI Enhancement
- Added an interactive help menu for better user guidance
- Users can now type `help` at any time to view available ciphers and commands
- Improved CLI interface for a more intuitive experience

### ✅ Day 6: ROT13 Cipher
- A simple Caesar-based cipher that shifts letters by 13
- Same function used for both encryption and decryption
- Use command: `R13`

### ✅ Day 7: Playfair Cipher
- Implemented Playfair Cipher encryption and decryption
- The cipher uses a 5x5 matrix based on a keyword to encode pairs of letters
- Integrated Playfair Cipher into the CLI tool

#### How to Use
- Choose the `PF` option in the menu
- Input the message and a keyword
- The message will be encrypted or decrypted based on your choice

#### Example:
- **Input**: `HELLO WORLD`
- **Keyword**: `KEYWORD`
- **Encrypted Output**: `KEMCR HOLOV`

### ✅ Day 8: Transposition Cipher
- Implemented Columnar Transposition encryption and decryption
- Integrated into the main CLI tool with keyword input

### ✅ Day 9: Playfair Cipher (Final Integration)
- Integrated Playfair Cipher into the CLI menu with interactive support
- Users can now encrypt/decrypt using the `PF` option directly from the CLI

---

## Usage

1. Clone the repository.
2. Run the `main.py` file.
3. Follow the prompts to encode or decode a message.

## Testing

To ensure the functionality of the algorithms, unit tests have been written and can be run with:

```bash
python test_crypto.py
