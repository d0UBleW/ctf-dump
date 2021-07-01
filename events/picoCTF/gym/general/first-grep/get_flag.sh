#!/bin/bash

strings file | grep --color=none -oE "picoCTF{.*}"
