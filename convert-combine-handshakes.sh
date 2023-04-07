#!/bin/bash

DIR="$1"
FILES=$DIR/*.pcap
for f in $FILES; do
  cap2hccapx.bin $f $f.hccapx
done
HCCAPX=$DIR/*.hccapx
for i in $HCCAPX; do
  cat "$i" >> $DIR/combined.hccapx
  rm "$i"
done
