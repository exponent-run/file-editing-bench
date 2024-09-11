#!/bin/bash

source "$(dirname "$0")/common.sh"

# Check if urls.txt exists
if [ ! -f "$URLS_FILE" ]; then
    echo "Error: $URLS_FILE not found. Please run the downloader script first."
    exit 1
fi

# Process each URL in urls.txt
while IFS= read -r url; do
    echo "Processing: $url"

    # Extract repository and file information
    read repo_owner repo_name _ file_path file_name <<< $(extract_info_from_url "$url")

    # Construct the folder path
    folder_path="${BASE_DIR}/${repo_owner}__${repo_name}__${file_name%.*}"

    # Check if the folder exists
    if [ ! -d "$folder_path" ]; then
        echo "Warning: Folder not found for $url. Skipping..."
        continue
    fi

    # Path to the original file
    original_file="$folder_path/$file_name"

    # Download and overwrite the original file
    download_file "$url" "$original_file"

    # Path to the modified file
    file_extension="${file_name##*.}"
    modified_file="$folder_path/${file_name%.*}.after.$file_extension"

    # Path to the diff file
    diff_file="$folder_path/${file_name%.*}.diff"

    # Generate the diff
    generate_diff "$original_file" "$modified_file" "$diff_file"

    echo "Generated diff for $file_name"
    echo "----------------------------"
done < "$URLS_FILE"

echo "All diffs have been generated."
