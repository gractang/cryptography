import string
# import this

# Caesar Cipher

def build_corresponding(offset):
    normal = string.ascii_uppercase
    shifted = normal[offset:] + normal[:offset]
    return shifted

# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    shifted = build_corresponding(offset)
    ciphertext = ""
    for ch in plaintext:
        if ch.isalpha():
            ciphertext += shifted[ord(ch)-ord('A')]
        else:
            ciphertext += ch
    return ciphertext


# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    pass

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    print(encrypt_caesar("PYTHON!", 3))
    pass

if __name__ == "__main__":
    main()
