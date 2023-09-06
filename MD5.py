import hashlib

def generate_sha256(input):
    sha256 = hashlib.sha256()
    sha256.update(input.encode())
    return sha256.hexdigest()


input = "chinwe "
display_sha256 = generate_sha256(input)
print(f"sha256 Hash: {display_sha256}")

#ebb17344b09005b2bfe462d07256a4a61988c2a792cc8ed10828481eca6b8933 chinwe without space
#95dd31e2d303f62b8f4756115b1325da5c6c5a03cda3c730c0afbe4159a06ac0 chinwe with space

