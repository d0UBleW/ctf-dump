#!/bin/bash


curl -s https://metaproblems.com/2841e99cee26f773b26b300acad556c4/inspect/ | grep Jazz | grep -oP "MetaCTF{.*?}"
