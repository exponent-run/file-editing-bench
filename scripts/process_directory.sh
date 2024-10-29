#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: Directory $1 does not exist"
    exit 1
fi

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Process each file in the directory
for file in "$1"/*; do
    if [ -f "$file" ]; then
        echo "Processing file: $file"
        "$SCRIPT_DIR/input_prompt.sh" "$file"
	git reset --hard origin/main
	git clean -fd
    fi
done
