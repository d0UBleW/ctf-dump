#!/bin/bash


strings ./strings | grep -oP "MetaCTF{.*}"
