#!/bin/bash

strings flag.zip | grep --color=none -oE "nactf{.*}"
