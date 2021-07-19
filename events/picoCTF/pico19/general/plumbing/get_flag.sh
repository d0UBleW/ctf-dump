#!/bin/bash

nc jupiter.challenges.picoctf.org 7480 << EOF | grep -io picoctf{.*}
