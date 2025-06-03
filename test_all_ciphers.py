import unittest
from caesar_cipher import caesar_encrypt, caesar_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from base64_cipher import base64_encode, base64_decode
from playfair_cipher import playfair_encrypt, playfair_decrypt
from affine_cipher import affine_encrypt, affine_decrypt
from rot13_cipher import rot13_cipher
from rail_fence_cipher import rail_fence_encrypt, rail_fence_decrypt
from columnar_transposition import columnar_encrypt, columnar_decrypt
from hill_cipher import hill_encrypt, hill_decrypt
from atbash_cipher import atbash_cipher

class TestCiphers(unittest.TestCase):

    def test_caesar(self):
        text = "HELLO"
        shift = 3
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        self.assertEqual(decrypted, text)

    def test_vigenere(self):
        text = "HELLO"
        key = "KEY"
        encrypted = vigenere_encrypt(text, key)
        decrypted = vigenere_decrypt(encrypted, key)
        self.assertEqual(decrypted, text)

    def test_base64(self):
        text = "HELLO"
        encoded = base64_encode(text)
        decoded = base64_decode(encoded)
        self.assertEqual(decoded, text)

    def test_playfair(self):
        text = "HELLO"
        key = "KEYWORD"
        encrypted = playfair_encrypt(text, key)
        decrypted = playfair_decrypt(encrypted, key)
        self.assertEqual(decrypted.replace('X', ''), text)  # Allowing padding

    def test_affine(self):
        text = "HELLO"
        a, b = 5, 8
        encrypted = affine_encrypt(text, a, b)
        decrypted = affine_decrypt(encrypted, a, b)
        self.assertEqual(decrypted, text)

    def test_rot13(self):
        text = "HELLO"
        encrypted = rot13_cipher(text)
        decrypted = rot13_cipher(encrypted)
        self.assertEqual(decrypted, text)

    def test_rail_fence(self):
        text = "HELLO"
        rails = 3
        encrypted = rail_fence_encrypt(text, rails)
        decrypted = rail_fence_decrypt(encrypted, rails)
        self.assertEqual(decrypted, text)

    def test_columnar(self):
        text = "HELLO"
        key = "KEY"
        encrypted = columnar_encrypt(text, key)
        decrypted = columnar_decrypt(encrypted, key)
        self.assertEqual(decrypted.replace('X', ''), text)  # Allowing padding

    def test_hill(self):
        text = "HELP"
        encrypted = hill_encrypt(text)
        decrypted = hill_decrypt(encrypted)
        self.assertEqual(decrypted, text)

    def test_atbash(self):
        text = "HELLO"
        encrypted = atbash_cipher(text)
        decrypted = atbash_cipher(encrypted)
        self.assertEqual(decrypted, text)

if __name__ == "__main__":
    unittest.main()
