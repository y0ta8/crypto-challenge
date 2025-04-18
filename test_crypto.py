import unittest
from caesar_cipher import caesar_encrypt, caesar_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from base64_cipher import base64_encode, base64_decode

class TestCryptoMethods(unittest.TestCase):

    # Caesar Cipher Tests
    def test_caesar_encrypt(self):
        self.assertEqual(caesar_encrypt("HELLO", 3), "KHOOR")
    
    def test_caesar_decrypt(self):
        self.assertEqual(caesar_decrypt("KHOOR", 3), "HELLO")

    # Vigenère Cipher Tests
    def test_vigenere_encrypt(self):
        self.assertEqual(vigenere_encrypt("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_vigenere_decrypt(self):
        self.assertEqual(vigenere_decrypt("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    # Base64 Tests
    def test_base64_encode(self):
        self.assertEqual(base64_encode("Hello, World!"), "SGVsbG8sIFdvcmxkIQ==")

    def test_base64_decode(self):
        self.assertEqual(base64_decode("SGVsbG8sIFdvcmxkIQ=="), "Hello, World!")

    # Edge Case Tests
    def test_empty_string_caesar(self):
        self.assertEqual(caesar_encrypt("", 5), "")
        self.assertEqual(caesar_decrypt("", 5), "")

    def test_empty_string_vigenere(self):
        self.assertEqual(vigenere_encrypt("", "KEY"), "")
        self.assertEqual(vigenere_decrypt("", "KEY"), "")

    def test_empty_string_base64(self):
        self.assertEqual(base64_encode(""), "")
        self.assertEqual(base64_decode(""), "")

if __name__ == '__main__':
    unittest.main()
