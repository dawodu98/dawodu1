from cryptography.fernet import Fernet

# Function to generate a random symmetric key
def generate_symmetric_key():
    return Fernet.generate_key()

# Function to encrypt the password using the symmetric key
def encrypt_password(symmetric_key, password):
    cipher_suite = Fernet(symmetric_key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Get the user's password as input
user_password = input("Enter your password: ")

# Generate a random symmetric key
symmetric_key = generate_symmetric_key()

# Encrypt the user's password
encrypted_password = encrypt_password(symmetric_key, user_password)

# Display the encrypted password
print(f"Encrypted Password: {encrypted_password.decode()}")
