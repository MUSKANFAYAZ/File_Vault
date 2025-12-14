                         FileVault - Secure File Encryption Locker
FileVault is a powerful and secure command-line tool for encrypting and decrypting files locally. It uses modern, authenticated encryption algorithms and a secure key management system to ensure your data stays private and tamper-proof.

Features
Modern Encryption Algorithms: Choose between industry-standard AES-256-GCM and the fast, modern ChaCha20-Poly1305.

Authenticated Encryption (AEAD): All ciphers provide built-in integrity checks, protecting your files from tampering.

Dual Encryption Modes:

Password-Based: Simple and effective encryption using a password you provide.

Asymmetric (Public Key): Encrypt files for a recipient using their public RSA key. They are the only one who can decrypt it with their private key.

Secure Key Derivation: Uses Argon2id, a state-of-the-art, memory-hard hashing algorithm to protect your passwords against brute-force attacks.

Secure File Deletion: Option to securely overwrite and delete the original plaintext file after encryption, preventing data recovery.

Performance Benchmarking: A built-in tool to measure and compare the performance of the encryption algorithms on your machine.

Installation
To get started with FileVault, you'll need Python 3.8 or newer.

Clone the repository:

git clone [https://github.com/your_username/filevault.git](https://github.com/your_username/filevault.git)
cd filevault

(Remember to replace your_username/filevault with the actual URL of your repository)

Create a Virtual Environment (Recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies and the tool:
This command installs all required libraries and also creates the filevault command-line tool.

pip install -e .

Quick Start & Usage
FileVault is now installed. You can run all commands by starting with filevault.

1. Generating a Key Pair (for Asymmetric Encryption)
Create a new 2048-bit RSA key pair. You will be prompted for a password to protect your private key.

filevault genkey my_keys

This creates my_keys_pub.pem (your public key, safe to share) and my_keys_priv.pem (your private key, keep it secret!).

2. Encrypting a File
Using a Recipient's Public Key
Encrypt my_secret_document.txt for someone using their public key. No password is required for the file itself.

filevault encrypt my_secret_document.txt --recipient-key my_keys_pub.pem

Using a Password
Encrypt the file with a password. You will be prompted to enter it securely.

filevault encrypt my_secret_document.txt

Encryption Options
Choose an algorithm (AES is the default):

filevault encrypt my_secret_document.txt --algo chacha

Securely delete the original file after encryption:

filevault encrypt my_secret_document.txt --delete

This will create an encrypted file named my_secret_document.txt.fvault.

3. Decrypting a File
Using Your Private Key
If the file was encrypted for you, use your private key to decrypt it. You'll be prompted for the password that protects your key.

filevault decrypt my_secret_document.txt.fvault --private-key my_keys_priv.pem

Using a Password
If the file was encrypted with a password, you'll be prompted to enter it.

filevault decrypt my_secret_document.txt.fvault

This will restore the original file, e.g., my_secret_document.txt.

4. Running Benchmarks
Measure and compare encryption algorithm performance.

# Run a benchmark on both algorithms with 50MB of data
filevault benchmark

# Run a benchmark on AES with 200MB of data
filevault benchmark --size 200 --algo aes

Running Tests
To ensure everything is working correctly, you can run the built-in unit tests.

python -m unittest discover tests

License
This project is licensed under the MIT License. See the LICENSE file for details.
