import string
# import this

# Caesar Cipher

# Builds a corresponding shifted "alphabet"
# to reference in Caesar cipher encoder
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
    return encrypt_caesar(ciphertext, -offset)

# Vigenere Cipher

# Makes a key— truncated if keyword is longer than plaintext,
# padded if keyword is shorter
def make_key(plaintext, keyword):
    key = ""
    pos = 0
    while len(plaintext) > len(key):
        key += keyword[pos]
        pos += 1
        pos %= len(keyword)
    return key

# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    key = make_key(plaintext, keyword)
    pos = 0
    ciphertext = ""
    for ch in plaintext:
        offset = ord(key[pos])-ord('A')
        index = (ord(ch) + offset)

        # Do the wrapping thing
        ch_new = chr(index) if index-ord('A') < 26 else chr(index-26)
        ciphertext += ch_new
        pos += 1
    return ciphertext

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    key = ""
    for ch in keyword:
        index = ord(ch)-ord('A')
        key += string.ascii_uppercase[len(string.ascii_uppercase)-index]
    return encrypt_vigenere(ciphertext, key)

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
    # print(encrypt_caesar("PYTHON!", 3))
    # print(decrypt_caesar("SBWKRQ", 3))
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

if __name__ == "__main__":
    main()
