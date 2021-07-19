#!/bin/bash

srch_strings dds1-alpine.flag.img | grep -i picoCTF{.*} | rev | cut -d " " -f1 | rev
