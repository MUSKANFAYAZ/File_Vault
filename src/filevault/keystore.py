from Crypto.PublicKey import RSA

def generate_key_pair(base_filename, password):
    """
    Generates a 2048-bit RSA key pair and saves them to PEM files.
    """
    try:
        # Generate the key object
        key = RSA.generate(2048)

        # Export and save the private key, encrypted with the provided password
        private_key_pem = key.export_key(passphrase=password, pkcs=8,
                                         protection="scryptAndAES128-CBC")
        private_key_file = f"{base_filename}_priv.pem"
        with open(private_key_file, "wb") as f:
            f.write(private_key_pem)

        # Export and save the public key
        public_key_pem = key.publickey().export_key()
        public_key_file = f"{base_filename}_pub.pem"
        with open(public_key_file, "wb") as f:
            f.write(public_key_pem)

        print(f"✅ Key pair generated successfully!")
        print(f"   -> Public Key: {public_key_file}")
        print(f"   -> Private Key: {private_key_file}")
        return True

    except Exception as e:
        print(f"❌ Error generating key pair: {e}")
        return False