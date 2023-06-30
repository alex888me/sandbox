#!/bin/bash

logdir="path/to/log/files" # replace with your log directory

cd $logdir

declare -A fileDates

# For each file...
for file in *; do
    # Extract the modification date, ignoring the time.
    date=$(date -r "$file" +%F)

    # If this date is not in the associative array, or this file is newer than
    # the one that's in the array, add it to the array.
    if [[ ! ${fileDates[$date]} ]] || [[ "$file" -nt "${fileDates[$date]}" ]]; then
        fileDates[$date]="$file"
    fi
done

# Now, for each date in the associative array, sorted in reverse order...
for date in $(echo ${!fileDates[@]} | tr ' ' '\n' | sort -r); do
    # If there are more than 5 dates in the array, delete the file
    # associated with the earliest date.
    if [[ ${#fileDates[@]} -gt 5 ]]; then
        rm "${fileDates[$date]}"
        unset fileDates[$date]
    fi
done

# Delete all files in the log directory that are not in the associative array.
for file in *; do
    if [[ ! ${fileDates[*]} =~ $file ]]; then
        rm "$file"
    fi
done
