#!/usr/bin/env python3
import sys
import argparse
import urllib.parse
from pathlib import Path

def full_url_encode(input_str):
    """
    Encodes every character using percent-encoding.
    Example: "Hi!" -> "%48%69%21"
    """
    return ''.join(f'%{ord(char):02X}' for char in input_str)

def selective_url_encode(input_str):
    """
    Encodes only characters that require escaping in URLs.
    Example: "Hello, world!" -> "Hello%2C%20world%21"
    """
    return urllib.parse.quote(input_str, safe='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~')

def url_decode(input_str):
    """
    Decodes any percent-encoded string.
    """
    return urllib.parse.unquote(input_str)

def parse_arguments():
    """
    Sets up and parses command-line arguments using argparse.
    Returns the parsed arguments as a Namespace object.
    """
    parser = argparse.ArgumentParser(
        description="URL-encode or decode input from stdin, file, or string input."
    )

    # Mutually exclusive group for mode selection
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--encode", "-e", action="store_true",
        help="Encode input (special characters only, by default)"
    )
    group.add_argument(
        "--decode", "-d", action="store_true",
        help="Decode percent-encoded input"
    )

    # Optional input methods
    parser.add_argument(
        "--input", "-i", type=str,
        help="Input string provided directly as an argument"
    )
    parser.add_argument(
        "--file", "-f", type=str,
        help="Path to a file to read input from"
    )

    # Optional full-encode flag
    parser.add_argument(
        "--full-encode", action="store_true",
        help="When encoding, encode every character (not just special characters)"
    )

    return parser.parse_args()

def read_input(args):
    """
    Reads input from one of: --input, --file, or stdin.
    Removes trailing newline and uses the input as-is to avoid shell metacharacter issues.
    """
    if args.input is not None:
        return args.input.strip('\n')
    elif args.file is not None:
        path = Path(args.file)
        if not path.exists():
            sys.exit(f"Error: File '{args.file}' not found.")
        return path.read_text(encoding='utf-8').strip('\n')
    elif not sys.stdin.isatty():
        return sys.stdin.read().strip('\n')
    else:
        sys.exit("Error: No input provided. Use --input, --file, or pipe input via stdin.")

def main():
    args = parse_arguments()
    input_data = read_input(args)

    if args.encode:
        if args.full_encode:
            result = full_url_encode(input_data)
        else:
            result = selective_url_encode(input_data)
    elif args.decode:
        result = url_decode(input_data)
    else:
        sys.exit("Error: You must specify either --encode or --decode.")

    print(result)

if __name__ == "__main__":
    main()
