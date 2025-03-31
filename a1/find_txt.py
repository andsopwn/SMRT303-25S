import os

def merge_txt_in_hidden(hidden_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as out:
        for root, dirs, files in os.walk(hidden_dir):
            for filename in files:
                if filename.lower().endswith('.txt'):
                    txt_path = os.path.join(root, filename)
                    try:
                        with open(txt_path, 'r', encoding='utf-8') as f:
                            contents = f.read()
                        out.write(contents)
                        out.write('\n')
                    except Exception as e:
                        print(f"Error reading {txt_path}: {e}")

if __name__ == "__main__":
    hidden_directory = "hidden"
    merged_output    = "merge.txt"
    merge_txt_in_hidden(hidden_directory, merged_output)
    print(f"{hidden_directory} -> '{merged_output}' Merged.")
