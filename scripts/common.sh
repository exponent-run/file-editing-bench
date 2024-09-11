#!/bin/bash

# Shared variables
URLS_FILE="urls.txt"
BASE_DIR="file_editing_bench"

# Function to add URL to urls.txt and keep it sorted
add_url_to_file() {
    local url="$1"
    if [ ! -f "$URLS_FILE" ]; then
        echo "$url" > "$URLS_FILE"
    else
        echo "$url" >> "$URLS_FILE"
        sort -u "$URLS_FILE" -o "$URLS_FILE"
    fi
}

# Function to download a file from a GitHub URL
download_file() {
    local url="$1"
    local output_file="$2"
    local raw_url=$(echo "$url" | sed 's|github.com|raw.githubusercontent.com|' | sed 's|/blob/|/|')
    curl -s -L "$raw_url" > "$output_file"
}

# Function to get the latest commit hash for a branch
get_latest_commit() {
    local repo_url="$1"
    local branch="$2"
    curl -s "https://api.github.com/repos/${repo_url}/commits/${branch}" | grep '"sha":' | head -n 1 | awk -F'"' '{print $4}'
}

# Function to generate a diff between two files
generate_diff() {
    local original_file="$1"
    local modified_file="$2"
    local diff_file="$3"

    # Generate diff
    diff -u "$original_file" "$modified_file" > "$diff_file.tmp"

    # Remove timestamps from the diff headers
    sed '1,2s/\t.*$//' "$diff_file.tmp" > "$diff_file"

    # Clean up temporary file
    rm "$diff_file.tmp"
}

# Function to extract repository and file information from URL
extract_info_from_url() {
    local url="$1"
    local repo_owner=$(echo "$url" | awk -F'/' '{print $4}')
    local repo_name=$(echo "$url" | awk -F'/' '{print $5}')
    local branch_or_commit=$(echo "$url" | awk -F'/' '{print $7}')
    local file_path=$(echo "$url" | awk -F'/blob/' '{print $2}' | cut -d'/' -f2-)
    local file_name=$(basename "$file_path")
    echo "$repo_owner" "$repo_name" "$branch_or_commit" "$file_path" "$file_name"
}

