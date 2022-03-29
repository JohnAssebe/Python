#!/bin/bash
>oldFiles.txt
janes=$(grep -i " jane " ../data/list.txt | cut -d ' ' -f 3)
for jane in $janes;do
if test -e ~/$jane;then
echo $jane >> oldFiles.txt;
fi
done;
