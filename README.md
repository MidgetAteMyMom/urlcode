# URL Encoder/Decoder

A Python command-line tool to encode or decode URL strings from standard input, command-line arguments, or files.

## Features

- ✅ Encode only special characters (default behavior)
- 🔐 Encode every character (`--full-encode`)
- 🔓 Decode URL-encoded strings
- 📥 Accept input from:
  - `--input` (string from CLI)
  - `--file` (read input from file)
  - `stdin` (piped input)
  
## Usage

```bash
# Basic encoding (only special characters)
python3 urlcoder.py --encode --input "Hello, world!"
# Output: Hello%2C%20world%21

# Full encoding of every character
python3 urlcoder.py --encode --full-encode --input "Hello"
# Output: %48%65%6C%6C%6F

# Decoding
python3 urlcoder.py --decode --input "Hello%2C%20world%21"
# Output: Hello, world!

# Using input from a file
python3 urlcoder.py --encode --file input.txt

# Using piped input
echo "Hello, world!" | python3 urlcoder.py --encode
