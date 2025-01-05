#!/usr/bin/env bash
#
# Usage: bin/extract_names

filename="$1"
exec < "$filename"
read header

amazon_workers=()
while IFS="," read -r id l_name f_name email price country
do
    if [[ "$email" == *"Amazon.com" || "$email" == *"amazon.com" ]];
    then
        amazon_workers+=("$f_name $l_name")
    fi
done
printf "%s\n" "${amazon_workers[@]}" > "names_output.txt"