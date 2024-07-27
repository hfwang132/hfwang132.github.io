import argparse

def replace_keywords_in_file(file_path, replacements):
    """
    Replace keywords in a file with new keywords.

    Parameters:
    file_path (str): The path to the file where replacements are to be made.
    replacements (dict): A dictionary where keys are the old keywords and values are the new keywords.

    Returns:
    None
    """
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Replace the keywords
    for old_word, new_word in replacements.items():
        file_content = file_content.replace(old_word, new_word)

    try:
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)
    except Exception as e:
        print(f"Error writing file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Replace keywords in a file with new keywords.")
    parser.add_argument('file_path', type=str, help='The path to the file where replacements are to be made.')
    args = parser.parse_args()

    # Define the replacements dictionary here
    replacements = {
        r'_': r'\_',
        r'\\': r'\\\\',
        r'\#': r'#',
        r'\.': r'.',
        r'\-': r'-',
        r'\[#ref\\\\_1](#ref\\\\_1\)': r'[1]',
        r'\[#ref\\\\_2](#ref\\\\_2\)': r'[2]',
        r'\[#ref\\\\_3](#ref\\\\_3\)': r'[3]',
        r'\(': r'(',
        r'\[': r'[',
        r'\)': r')',
        r'\]': r']',
        r'*': r'\*',
        r'\*\*': r'**'
    }

    print(f"File path: {args.file_path}")
    print(f"Replacements: {replacements}")

    replace_keywords_in_file(args.file_path, replacements)

if __name__ == '__main__':
    main()
