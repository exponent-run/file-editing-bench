#!/bin/bash

source "$(dirname "$0")/common.sh"

read -p "Enter the Github URL to file: " github_url

# Check if the URL is a valid GitHub link
if [[ ! $github_url =~ ^https://github.com/ ]]; then
    echo "The provided URL is not a valid GitHub link."
    exit 1
fi

# Extract information from URL
read repo_owner repo_name branch_or_commit file_path file_name <<< $(extract_info_from_url "$github_url")

# Generate permalink if the URL points to a branch
if [[ $branch_or_commit != "" && ! $branch_or_commit =~ ^[0-9a-f]{40}$ ]]; then
    latest_commit=$(get_latest_commit "${repo_owner}/${repo_name}" "$branch_or_commit")
    permalink="${github_url%/blob/*}/blob/${latest_commit}/${file_path}"
else
    permalink="$github_url"
fi

echo "Repository: $repo_owner/$repo_name"
echo "File name: $file_name"
echo "Permalink: $permalink"

# Add the permalink to urls.txt
add_url_to_file "$permalink"

# Create the folder to save the file
folder_to_save_to="${BASE_DIR}/${repo_owner}__${repo_name}__${file_name%.*}"
mkdir -p "$folder_to_save_to"

# Download the file
download_file "$permalink" "$folder_to_save_to/$file_name"

# Create a copy of the file
file_extension="${file_name##*.}"
cp "$folder_to_save_to/$file_name" "$folder_to_save_to/${file_name%.*}.after.$file_extension"

# Create instructions.md
cat <<EOL > "$folder_to_save_to/instructions.md"
1. Edit the file \`$file_name\` so that:
EOL

echo "File downloaded and instructions created in $folder_to_save_to"
echo "Permalink added to $URLS_FILE"
