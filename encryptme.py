
import string
import random
from base64 import b64encode, b64decode

# Temporary test message
secret = 'Hello my name is Oskar'

secret_encoding = ['step1', 'step2', 'step3']


# Step 1: Substitution cipher
def step1(s):
    _step1 = str.maketrans(
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON"
    )
    return s.translate(_step1)


# Step 2: Base64 encoding
def step2(s):
    return b64encode(s.encode('utf-8')).decode('ascii')


# Step 3: Caesar cipher (shift of 4)
def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)


# Main encryption function
def make_secret(plain, count):
    a = '2{}'.format(b64encode(plain.encode('utf-8')).decode('ascii'))

    for _ in range(count):
        r = random.choice(secret_encoding)
        si = secret_encoding.index(r) + 1
        _a = globals()[r](a)
        a = '{}{}'.format(si, _a)

    return a


if __name__ == '__main__':
    print(make_secret(secret, count=5))
