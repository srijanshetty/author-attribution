#!/bin/zsh

# Create a new folder for the supplied folder and split its corpus
mkdir ${1}.split
cd ${1}.split
cat ../${1}/*| tr "\n" " " | sed 's/\xe0\xa5\xa4//g' | sed 's/\xe2\x80\x98//g' | sed 's/\xe2\x80\x99//g' \
    | tr "[',?;\")(.!]" " " | sed 's/  */\n/g' | split -l 500
cd ..
