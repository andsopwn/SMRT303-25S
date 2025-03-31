import sys

def key_xor(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        data = f_in.read()
    
    key = bytes([0x12, 0x55])
    out = bytearray(len(data))
    
    for i, b in enumerate(data):
        out[i] = b ^ key[i % 2]
    
    with open(output_path, 'wb') as f_out:
        f_out.write(out)

def main():
    if len(sys.argv) != 3:
        print(f"usage -> {sys.argv[0]} <in> <out>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    key_xor(input_file, output_file)

if __name__ == "__main__":
    main()
