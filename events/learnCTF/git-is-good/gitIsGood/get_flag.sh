#!/bin/bash

git log -u | grep --color=none -oE flag{.*}
