# Decoder for challenge lab encrypted evidence file
import base64
import binascii
import os
import string
import sys

# intercepted.txt must be in the same folder as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "intercepted.txt")

PREVIEW_LEN = 70  # max characters shown per layer

LOWER = string.ascii_lowercase

STEP1_TABLE = str.maketrans(
    "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
    "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")

# rot13 reused reverses itself
def reverse_step1(s):
    return s.translate(STEP1_TABLE)

# reverses base64
def reverse_step2(s):
    return base64.b64decode(s, validate=True).decode("utf-8")


STEP3_TABLE = str.maketrans(LOWER, LOWER[4:] + LOWER[:4]) # encoder's table: a->e
STEP3_UNDO = {v: k for k, v in STEP3_TABLE.items()} # flipped: e->a

# reverses Caesar +4 (shifts back 4)
def reverse_step3(s):
    return s.translate(STEP3_UNDO)


UNDO_STEPS = {"1": reverse_step1, "2": reverse_step2, "3": reverse_step3}
NAMES = {"1": "ROT13", "2": "Base64", "3": "Caesar +4"}

# read the encrypted message from the file
try:
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        msg = f.read().strip()
except FileNotFoundError:
    print(f"Couldn't find {INPUT_FILE}")
    sys.exit(1)

print(f"Read {len(msg):,} characters from intercepted.txt\n")

layers = 0

# IMPORTANT: if the plaintext starts with 1 or 3, rot13/caesar will wrongly run on it, check the printed layers
while msg and msg[0] in UNDO_STEPS:
    tag = msg[0]
    try:
        msg = UNDO_STEPS[tag](msg[1:])
    except (binascii.Error, UnicodeDecodeError, ValueError):
        break  # Base64 failed -> msg is the plaintext
    layers += 1

    preview = msg if len(msg) <= PREVIEW_LEN else msg[:PREVIEW_LEN - 3] + "..."
    print(f"[{layers:>3}] {tag} {NAMES[tag]:<9} {len(msg):>9,} chars  -> {preview}")

print(f"\nPlaintext: {msg}")
print(f"Layers peeled: {layers}")