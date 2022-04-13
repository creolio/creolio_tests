#!/bin/bash

VERSION_HASH=$(git log --format="%H" -n 1)
VERSION_TIMESTAMP=$(git log -1 --format=%cd)

cp example.html example2.html

sed -i "s/@version/$VERSION_HASH/" example2.html
sed -i "s/@timestamp/$VERSION_TIMESTAMP/" example2.html
