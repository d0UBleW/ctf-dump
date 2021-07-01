#!/bin/bash

convert fixed.gif out%01d.png && cp out0.png atmp.png && ls *.png | while read img; do convert $img -transparent white _$img; convert _$img _atmp.png -gravity center -composite _atmp.png; done && convert -flatten _atmp.png flag.png && rm -rf _* && rm -rf out*.png && rm -rf atmp.png && eog flag.png && rm -rf flag.png && echo "ZmxhZ3tnMWZfb3JfajFmfQ==" | base64 -d; echo
