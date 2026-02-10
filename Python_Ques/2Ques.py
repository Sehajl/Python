import hashlib
def hash_file(file_name):
    """Generate SHA-1 hash of a file"""
    h = hashlib.sha1()

    with open(file_name, "rb") as file:
        while True:
            chunk = file.read(1024)  # Read file in 1024-byte chunks
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


# File names
file1 = "Resume_t.pdf"
file2 = "Resume_t.pdf"

# Generate hashes
hash1 = hash_file(file1)
hash2 = hash_file(file2)

# Compare hashes
if hash1 == hash2:
    print("These files are identical")
else:
    print("These files are not identical")

