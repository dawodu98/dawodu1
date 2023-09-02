from cryptography.fernet import Fernet

# Generate a random symmetric key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt user input
plaintext = input("Enter your message: ").encode()
ciphertext = cipher_suite.encrypt(plaintext)

print(f"Ciphertext: {ciphertext.hex()}")
