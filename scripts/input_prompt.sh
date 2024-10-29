#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file.txt>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File $1 does not exist"
    exit 1
fi

# Read the file content and escape any special characters
PROMPT_CONTENT=$(cat "$1" | sed 's/"/\\"/g')

exponent shell --autorun --headless --prod --depth 20 --prompt "$PROMPT_CONTENT"
