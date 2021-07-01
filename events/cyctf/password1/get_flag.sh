#!/bin/bash

cat tet.py | sort -n -k1 | rev | cut -d " " -f1 | tr -d "\n"; echo