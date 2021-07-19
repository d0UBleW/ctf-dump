#!/bin/bash

./warm -h | rev| cut -d " " -f1 | rev
