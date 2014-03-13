#!/bin/zsh

# Create a new folder for the supplied folder and split its corpus
mkdir ${1}.folder
cd ${1}.folder
cat ../${1}/* | split -l 200 

# Filter out punctuation marks and then count the frequencies
for file in *; do
    cat $file | sed 's/\xe0\xa5\xa4/ /g' | sed 's/\xe2\x80\x98/ /g' | sed 's/\xe2\x80\x99/ /g' \
        | tr "[',?;\")(.!]" " " | tr "[:blank:]" "\n" | sort | uniq -c | sort -nr > ${file}.txt
    rm -f ${file}
done
