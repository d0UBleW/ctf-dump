#!/bin/bash

strings turnip-for-what.jpg | grep --color=none -oE "nactf{.*}"
