#!/bin/bash


NUM=$1
IN="ex${NUM}"
OUT="dec${NUM}"

cat $IN | tr -d "\n" | base64 -d > $OUT
