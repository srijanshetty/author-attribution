#!/bin/zsh

# cat ${1}/**/*(^/) > corpus.txt
cat $1 | sed 's/\xe0\xa5\xa4/ /g' | sed 's/\xe2\x80\x98/ /g' | sed 's/\xe2\x80\x99/ /g' \
    | tr "[',?;\")(.!]" " " | tr "[:blank:]" "\n" | sort | uniq -c | sort -nr
