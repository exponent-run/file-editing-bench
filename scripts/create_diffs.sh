#!/bin/bash

# Loop through all directories in file_editing_bench
for dir in file_editing_bench/*; do
    # Skip if not a directory
    [ ! -d "$dir" ] && continue
    # Find all .after.* files in current directory
    find "$dir" -maxdepth 1 -name "*.after.*" | while read after_file; do
        # Extract base name and extension
        base_name=$(basename "$after_file" | sed 's/\.after\./\./g')
        
        # Construct task file path
        task_file="$dir/task_files/$base_name"
        
        # Construct diff file path (next to .after. file)
        diff_file="${after_file%.after.*}.diff"
        
        # Create diff if both files exist
        if [ -f "$task_file" ] && [ -f "$after_file" ]; then
            echo "Creating diff file: $diff_file"
            git diff --no-index "$task_file" "$after_file" | tail -n +3 > "$diff_file" || true
        fi
    done
done