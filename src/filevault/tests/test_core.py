# tests/test_core.py

import unittest
import os
import sys

# This is a bit of a trick to help Python find your src code from the tests folder
# It adds the parent directory (filevault/) to the list of places Python looks for modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.filevault import core

class TestCoreEncryption(unittest.TestCase):

    def setUp(self):
        """This method runs before each test."""
        self.original_content = b"This is a top secret message for testing."
        self.test_file_path = "test_file.txt"
        self.encrypted_file_path = "test_file.txt.fvault"
        self.decrypted_file_path = "test_file_decrypted.txt"
        self.password = "super_strong_password_123"

        # Create a dummy file to encrypt
        with open(self.test_file_path, "wb") as f:
            f.write(self.original_content)

    def tearDown(self):
        """This method runs after each test to clean up."""
        files_to_remove = [
            self.test_file_path, 
            self.encrypted_file_path, 
            self.decrypted_file_path
        ]
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)

    def test_password_encryption_decryption_cycle(self):
        """Tests the full encrypt -> decrypt cycle using a password."""
        # 1. Encrypt the file
        encrypted_data = core.encrypt_file_with_password(
            self.test_file_path, "test_file.txt", self.password, "AES-256-GCM"
        )
        self.assertIsNotNone(encrypted_data, "Encryption returned nothing.")

        # 2. Decrypt the file
        decrypted_content, _ = core.decrypt_file(encrypted_data, password=self.password)
        self.assertIsNotNone(decrypted_content, "Decryption returned nothing.")

        # 3. VERIFY: Check if the decrypted content matches the original
        self.assertEqual(
            self.original_content, 
            decrypted_content,
            "Decrypted content does not match the original content!"
        )
        print("\n✅ Password encryption/decryption cycle test passed.")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()