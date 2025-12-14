import argparse
import os
from getpass import getpass
# NEW: Import the benchmark module
from . import core, keystore, utils, benchmark

def main():
    parser = argparse.ArgumentParser(prog="filevault", description="Encrypt and decrypt files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- (Encrypt, Decrypt, Genkey commands remain the same) ---
    p_encrypt = subparsers.add_parser("encrypt", help="Encrypt a file.")
    p_encrypt.add_argument("file", help="Path to the file to encrypt.")
    p_encrypt.add_argument("--recipient-key", help="Path to the recipient's public key for asymmetric encryption.")
    p_encrypt.add_argument("--algo", default="aes", choices=['aes', 'chacha'], help="Encryption algorithm (aes or chacha). Default: aes")
    p_encrypt.add_argument("--delete", action='store_true', help="Securely delete the original file after encryption.")

    p_decrypt = subparsers.add_parser("decrypt", help="Decrypt a file.")
    p_decrypt.add_argument("file", help="Path to the encrypted file to decrypt.")
    p_decrypt.add_argument("--private-key", help="Path to your private key for asymmetric decryption.")

    p_genkey = subparsers.add_parser("genkey", help="Generate a new RSA public/private key pair.")
    p_genkey.add_argument("keyname", help="Base name for the key files (e.g., 'my_keys' creates my_keys_pub.pem and my_keys_priv.pem)")

    # --- NEW: BENCHMARK COMMAND ---
    p_benchmark = subparsers.add_parser("benchmark", help="Run a performance benchmark.")
    p_benchmark.add_argument(
        "--size", 
        type=int, 
        default=50, 
        help="Size of data to test in MB (e.g., 50)."
    )
    p_benchmark.add_argument(
        "--algo", 
        type=str, 
        default="all", 
        choices=['aes', 'chacha', 'all'], 
        help="Algorithm to benchmark (aes, chacha, or all)."
    )
    # ----------------------------

    args = parser.parse_args()

    # ... (genkey, encrypt, decrypt logic remains the same) ...
    if args.command == "genkey":
        password = getpass("🔑 Enter a password to protect your private key: ")
        confirm_password = getpass("🔑 Confirm password: ")
        if password != confirm_password:
            print("❌ Passwords do not match!")
            return
        keystore.generate_key_pair(args.keyname, password)
        return

    elif args.command == "encrypt":
        if not os.path.exists(args.file):
            print(f"❌ File not found: {args.file}")
            return
        
        original_filename = os.path.basename(args.file)
        output_file = f"{args.file}.fvault"
        
        algo_map = {"aes": "AES-256-GCM", "chacha": "ChaCha20-Poly1305"}
        algorithm = algo_map[args.algo]
        
        try:
            if args.recipient_key:
                # Asymmetric encryption
                if not os.path.exists(args.recipient_key):
                    print(f"❌ Recipient key not found: {args.recipient_key}")
                    return
                encrypted_data = core.encrypt_file_with_key(args.file, original_filename, args.recipient_key, algorithm)
                print(f"🔒 File encrypted using public key (Algorithm: {algorithm})")
            else:
                # Password-based encryption
                password = getpass("🔑 Enter encryption password: ")
                encrypted_data = core.encrypt_file_with_password(args.file, original_filename, password, algorithm)
                print(f"🔒 File encrypted with password (Algorithm: {algorithm})")
            
            with open(output_file, 'wb') as f:
                f.write(encrypted_data)
            print(f"💾 Encrypted file saved: {output_file}")
            
            if args.delete:
                utils.secure_delete(args.file)
        
        except Exception as e:
            print(f"❌ Encryption failed: {e}")
        return

    elif args.command == "decrypt":
        if not os.path.exists(args.file):
            print(f"❌ File not found: {args.file}")
            return
        
        try:
            with open(args.file, 'rb') as f:
                encrypted_data = f.read()
            
            if args.private_key:
                # Asymmetric decryption
                if not os.path.exists(args.private_key):
                    print(f"❌ Private key not found: {args.private_key}")
                    return
                key_password = getpass("🔑 Enter private key password: ")
                plaintext, original_filename = core.decrypt_file(encrypted_data, private_key_path=args.private_key, private_key_pass=key_password)
            else:
                # Password-based decryption
                password = getpass("🔑 Enter decryption password: ")
                plaintext, original_filename = core.decrypt_file(encrypted_data, password=password)
            
            if plaintext:
                output_file = original_filename
                with open(output_file, 'wb') as f:
                    f.write(plaintext)
                print(f"📂 Decrypted file saved: {output_file}")
            
        except Exception as e:
            print(f"❌ Decryption failed: {e}")
        return

    # --- NEW: BENCHMARK LOGIC ---
    elif args.command == "benchmark":
        algo_map = {
            "aes": "AES-256-GCM",
            "chacha": "ChaCha20-Poly1305"
        }

        if args.algo == 'all':
            benchmark.run_benchmark(args.size, algo_map['aes'])
            benchmark.run_benchmark(args.size, algo_map['chacha'])
        else:
            benchmark.run_benchmark(args.size, algo_map[args.algo])
    # ----------------------------


if __name__ == "__main__":
    main()