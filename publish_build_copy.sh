#!/bin/sh

echo "___________Building____________"
pelican content -s publishconf.py

echo "___________Remove Old____________"
rm -r ../website/output

echo "___________Copy____________"
mkdir ../website/output
cp -r ./output/* ../website/output