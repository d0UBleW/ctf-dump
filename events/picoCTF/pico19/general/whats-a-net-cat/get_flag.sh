#!/bin/bash

# connect to jupiter.challenges.picoctf.org at port 64287

nc -C jupiter.challenges.picoctf.org 64287 << EOF | grep -io picoCTF{.*}
