import string
import random
import math
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

# Makes a superincreasing sequence of length length
def make_superincreasing_sequence(length):
    seq = [random.randint(1,10)]
    total = seq[0]
    for i in range(length - 1):
        seq.append(random.randint(total + 1, 2 * total))
        total += seq[i+1]
    q = random.randint(total+1, 2 * total)
    return (tuple(seq), q)

# Finds a number r that is coprime with q 
# i.e. gcd(r, q) == 1
def find_r(q):
    r = random.randint(2, q)
    while math.gcd(r, q) != 1:
        r = random.randint(2, q)
    return r

# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    W, Q = make_superincreasing_sequence(n)
    return (W, Q, find_r(Q))


# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    B = []
    W, Q, R = private_key
    for i in range(len(W)):
        B.append(R * W[i] % Q)
    return tuple(B)

def base_conversion(b1, b2, numb1, num_bits):
    numb2 = []
    for i in range(num_bits):
        current_power = b2**(num_bits-i-1)
        numb2.append(numb1 // current_power)
        numb1 %= current_power
    return numb2

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    base1 = 10
    base2 = 2
    all_Cs = []
    for ch in plaintext:
        asc = ord(ch)
        num_bits = 8
        ascb2 = base_conversion(base1, base2, asc, num_bits)
        c = 0
        for i in range(num_bits):
            c += ascb2[i] * public_key[i]
        all_Cs.append(c)
    return all_Cs

# finds the modular inverse
def find_mod_inverse(R, Q):
    q = Q 
    y = 0
    inv = 1
  
    if (q == 1) : 
        return 0
  
    while (R > 1) : 
        quo = R // q 
        t = q  
        q = R % q 
        R = t 
        t = y 
        y = inv - quo * y 
        inv = t 
  
    # Make inverse positive 
    if (inv < 0) : 
        inv += Q
  
    return inv

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W, Q, R = private_key
    S = find_mod_inverse(R, Q)
    cprimes = []
    plaintext = []
    for c in ciphertext:
        cprimes.append(c * S % Q)
    for cprime in cprimes:
        indices = set()
        for i in range(len(W)):
            current = W[len(W)-i-1]
            if current <= cprime:
                indices.add(len(W)-i)
                cprime -= current
        ascval = 0
        for i in indices:
            ascval += 2 ** (len(W)-i)
        plaintext.append(chr(ascval))
    return "".join(plaintext)


def main():
    # Testing code here
    # print(encrypt_caesar("PYTHON!", 3))
    # print(decrypt_caesar("SBWKRQ", 3))
    # print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    # print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

    # should print 38
    # print(find_mod_inverse(17, 43))

    # the below is the wikipedia example
    # W = (2, 7, 11, 21, 42, 89, 180, 354)
    # Q = 881
    # R = 588
    # private_key = (W, Q, R)
    # print(encrypt_mhkc("a", create_public_key(private_key)))
    # print(decrypt_mhkc([1129], private_key))

    private_key = generate_private_key()
    public_key = create_public_key(private_key)
    print(decrypt_mhkc(encrypt_mhkc("PLZWORK", public_key), private_key))

if __name__ == "__main__":
    main()
