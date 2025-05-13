# Parsing two hex dumps and XORing them to reveal potential ASCII plaintext

# First hex dump (cracked value)
hex1 = """
30 35 45 C2 08 62 EE FC 05 B1 1F 4D EB 91 ED 2A
22 1B 0E 53 50 E9 C0 4D 7E 6D A4 C2 C3 81 3B CC
67 68 98 D3 66 9F 3F 64 54 68 6B 53 3A 60 95 93
EB B2 2B E0 A7 16 50 EE 1A 59 F4 96 51 A0 2E AD
02 2D 7F 6C CE 39 46 B2 F6 8D 14 10 D4 67 71 34
27 B1 1B
"""

# Second hex dump (attached value)
hex2 = """
78 5E 73 CE 4B 4B CB 4A 4A 2D 54 B0 55 C8 53 28
48 4A 2C C8 4B 2F 4A CC 4B 2F 4B 4A 54 48 2A 56
50 AF 28 CA 31 54 57 C8 4B 2C 04 33 8D D4 01 88
2A 0F C4
"""

# Remove whitespace/newlines and convert to bytes
b1 = bytes.fromhex(hex1)
b2 = bytes.fromhex(hex2)

# Method 1: XOR up to the shorter length
res_zip = bytes(a ^ b for a, b in zip(b1, b2))

# Method 2: Repeat second dump as a key over the first dump
res_repeat = bytes(b1[i] ^ b2[i % len(b2)] for i in range(len(b1)))

# Helper to show printable ASCII characters
def to_printable(data):
    return ''.join(chr(x) if 32 <= x < 127 else '.' for x in data)

# Print results
print("=== XOR using pairing up to the shorter length ===")
print("Raw bytes:", res_zip)
print("Printable:", to_printable(res_zip))

print("\n=== XOR using repeating key ===")
print("Raw bytes:", res_repeat)
print("Printable:", to_printable(res_repeat))

