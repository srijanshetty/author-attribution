#!/bin/zsh

# Create a new folder for the supplied folder and split its corpus
mkdir ${1}.corpus
for folder in ${1}/**(/); do
    echo "Now Processing folder ${folder}"
    mkdir ${folder}.split
    cd ${folder}.split
    cat ../${folder}/*| tr "\n" " " | sed 's/\xe0\xa5\xa4//g' | sed 's/\xe2\x80\x98//g' | sed 's/\xe2\x80\x99//g' \
        | tr "[',?;\")(.!]" " " | sed 's/  */\n/g' | split -l 500
    cd ..
    mv ${folder}.split ${1}.corpus
done
