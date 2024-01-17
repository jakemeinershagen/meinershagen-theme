#!/bin/sh

echo "___________Building____________"
pelican content -s pelicanconf.py

echo "___________Serving____________"
pelican --listen