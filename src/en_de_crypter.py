import hashlib

def encrypt(master_password, plaintext):
    # Create a new SHA-256 hash object
    hash_obj = hashlib.sha256()

    # Update the hash object with the master password
    hash_obj.update(master_password.encode('utf-8'))

    # Use the resulting digest as the encryption key
    encryption_key = hash_obj.digest()

    # Convert the plaintext string to bytes
    plaintext_bytes = plaintext.encode('utf-8')

    # Use XOR encryption with the key to encrypt the plaintext
    ciphertext_bytes = bytes([plaintext_byte ^ encryption_key[i % len(encryption_key)]
                              for i, plaintext_byte in enumerate(plaintext_bytes)])

    # Return the encrypted ciphertext as a hexadecimal string
    return ciphertext_bytes.hex()

def decrypt(master_password, ciphertext):
    # Create a new SHA-256 hash object
    hash_obj = hashlib.sha256()

    # Update the hash object with the master password
    hash_obj.update(master_password.encode('utf-8'))

    # Use the resulting digest as the decryption key
    decryption_key = hash_obj.digest()

    # Convert the ciphertext hexadecimal string to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext)

    # Use XOR encryption with the key to decrypt the ciphertext
    plaintext_bytes = bytes([ciphertext_byte ^ decryption_key[i % len(decryption_key)]
                             for i, ciphertext_byte in enumerate(ciphertext_bytes)])

    # Convert the decrypted plaintext bytes to a string
    plaintext = plaintext_bytes.decode('utf-8')

    # Return the decrypted plaintext
    return plaintext


