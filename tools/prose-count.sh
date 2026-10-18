#!/bin/sh
# Usage: count.sh file.html  -> prose words and sentences (tags, math stripped)
sed -n '/<body>/,/<script>/p' "$1" | sed 's/<[^>]*>//g; s/\$\$[^$]*\$\$//g; s/\$[^$]*\$/X/g' | tr -s ' \n' ' ' | awk '{w=NF; s=gsub(/[.!?] /,"&"); print "words:", w, "sentences:", s}'
