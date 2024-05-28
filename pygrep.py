# Description: A simple Python script to grep for keywords in a file.
#!/usr/bin/env python3

import sys

def grep_keywords(output, *keywords):
    """
    Function to search for keywords in the output and print matching lines.
    
    Args:
        output (file): The file object containing the output.
        *keywords (str): Variable number of keywords to search for.
    """
    for line in output:
        for keyword in keywords:
            if keyword in line:
                print(line.strip())
                break

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 pygrep.py <output_file> <keyword1> <keyword2> ...")
        sys.exit(1)

    output_file = sys.argv[1]
    keywords = sys.argv[2:]

    with open(output_file, "r") as file:
        grep_keywords(file, *keywords)