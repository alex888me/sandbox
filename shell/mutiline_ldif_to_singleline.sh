#!/bin/bash

# Check if the correct number of arguments are given
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <input.ldif> <output.ldif>"
    exit 1
fi

input_file="$1"
output_file="$2"

# Check if the input file exists
if [[ ! -f "$input_file" ]]; then
    echo "Error: Input file '$input_file' not found!"
    exit 2
fi

# Process the file with awk
awk 'BEGIN { ORS=""; line="" } 
     !/^ / { if (line) print line "\n"; line=$0 } 
     /^ / { line=line $0 } 
     END { if (line) print line "\n" }' "$input_file" > "$output_file"

echo "Processing complete. Output saved to '$output_file'."
