# Lab 11 – Encrypted Evidence File (Challenge Lab)

## Overview

This project was completed as part of the Secure Communication and Cryptography module at TU Dublin.

The aim of the challenge was to recover an intercepted message using a partially damaged Python encryption script provided as part of a fictional Garda investigation.

The original encryption program contained missing values and outdated Python 2 syntax. Our task was to investigate how the program worked, restore its functionality, and develop a Python script capable of reversing the encoding operations to recover the original plaintext.

## Files

| File | Description |
|---|---|
| `encryptme.py` | Restored encryption script used to generate encoded messages. |
| `decrypter.py` | Python script that reverses the encoding operations and recovers plaintext. |
| `intercepted.txt` | Intercepted encoded message provided for the challenge. |
| `verification.txt` | Optional file containing newly generated ciphertext for verification. |

## Encoding Methods

The encryption program uses three different encoding methods:

**1. ROT13**

A substitution cipher that shifts letters by 13 positions. Applying ROT13 twice restores the original text.

**2. Base64**

Encodes the input into a Base64 string. This can be reversed using Python's `base64.b64decode()` function.

**3. Caesar Cipher (+4)**

Shifts lowercase letters forward by four positions in the alphabet. The decoder reverses this by shifting them backwards by four positions.

Each operation adds a numerical prefix identifying the method used:

- `1` – ROT13
- `2` – Base64
- `3` – Caesar shift (+4)

The encryption script randomly selects between these methods for the specified number of operations.

An initial Base64 encoding is always performed before the randomly selected operations.

## Requirements

- Python 3
- No additional libraries required

The scripts use Python's built-in libraries, so no external packages need to be installed.

## How to Run

### 1. Download the Files

Download or clone the repository and ensure the Python scripts and intercepted message are stored in the same directory.

### 2. Run the Encryption Script

Open `encryptme.py` and modify the plaintext message:

```python
secret = 'Why do elephants have big ears?'
```

Set the number of encoding operations at the bottom of the script:

```python
if __name__ == '__main__':
    print(make_secret(secret, count=67))
```

Run the script:

```bash
python encryptme.py
```

The program will generate an encoded message using randomly selected encoding methods.

**Note:** The output will vary between executions because the program uses `random.choice()`.

### 3. Run the Decryption Script

Ensure `intercepted.txt` is located in the same folder as `decrypter.py`.

Run:

```bash
python decrypter.py
```

The decoder reads the intercepted message and reverses each encoding operation based on its numerical prefix.

It also displays the operation used, the number of characters remaining, and a preview of the message after each layer.

## Results

The intercepted message was successfully decoded.

**Recovered plaintext:**

```text
Why do elephants have big ears?
```

**Recovered encoding count:** 67

**Total decoded layers:** 68

The additional layer comes from the initial Base64 encoding performed before the 67 randomly selected operations.

## Verification

To verify that both scripts worked correctly, the recovered plaintext was used as input for the encryption program with a count of 67.

The generated ciphertext can be saved in a separate file named `verification.txt`.

To decode this file, change the following line in `decrypter.py`:

```python
INPUT_FILE = os.path.join(SCRIPT_DIR, "verification.txt")
```

Then run the decoder again.

The expected output is:

```text
Plaintext: Why do elephants have big ears?
Layers peeled: 68
```

This verifies that the decoder can successfully reverse the operations performed by the encoder.

Because the encoding methods are randomly selected, the newly generated ciphertext will not necessarily match the original intercepted message.
**Institution:** Technological University Dublin
