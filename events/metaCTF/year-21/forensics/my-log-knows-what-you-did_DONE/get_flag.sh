#!/bin/bash


cat log | grep -oP "(?<=-enc ).*" | base64 -d | grep -oP "MetaCTF{.*?}"
