import hashlib

def generate_sha256(input):
    sha256 = hashlib.sha256()
    sha256.update(input.encode())
    return sha256.hexdigest()



input = "gomycode"
sha256_show = generate_sha256(input)
print(f"sha256 Hash: {sha256_show}")



