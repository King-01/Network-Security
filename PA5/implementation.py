# Python program to illustrate ElGamal encryption

import random
from math import pow, gcd

a = random.randint(2, 10)
l, r = pow(10, 28), pow(10, 60)
oq = {}
# Generating large random numbers
def generate_key(M):
    while True:
        random_trial = random.randint(l, M)
        if gcd(random_trial, M) == 1:
            return random_trial


# Modular exponentiation
def exponentiate_mod(a, p, M):
    x, y = 1, a
    while p > 0:
        if p & 1:
            x = (x * y) % M
        y = (y * y) % M
        p = p // 2

    return x % M


# Encrypts the message rec_text from receiver
def encrypt_message(rec_text, M, h, g):

    en_rec_text, k = [], generate_key(M)

    s, p = exponentiate_mod(h, k, M), exponentiate_mod(g, k, M)

    for i in range(0, len(rec_text)):
        en_rec_text.append(rec_text[i])
    for i in range(0, len(en_rec_text)):
        en_rec_text[i] = s * ord(en_rec_text[i])
    global oq
    oq["s"] = s
    return en_rec_text, p


# Decrypts the encrypted message en_rec_text from receiver
def decrypt_message(en_rec_text, p, key, M):

    dr_rec_text, h = [], exponentiate_mod(p, key, M)

    for i in range(0, len(en_rec_text)):
        dr_rec_text.append(chr(int(en_rec_text[i] / h)))

    return dr_rec_text


if __name__ == "__main__":
    rec_text = input("Enter the message to send - ")

    M = random.randint(pow(10, 20), pow(10, 50))
    g, key = random.randint(2, M), generate_key(M)
    # key - private key for receiver
    h = exponentiate_mod(g, key, M)
    # Encrypt the message from the sender
    en_rec_text, p = encrypt_message(rec_text, M, h, g)
    # Decrypt the encrypted message, once receiver receives it
    decrypted_rec_text = decrypt_message(en_rec_text, p, key, M)
    # Construct the decrypted text from array of strings
    decrypted_rec_text = "".join(decrypted_rec_text)

    print(
        "Received entry(Original message) - {}\ng value - {}\nh value - {}\np value - {}\ns value - {}\nDecrypted Message - {}".format(
            rec_text, g, h, p, oq["s"], decrypted_rec_text
        )
    )
