#!/bin/bash
x=1
filename="chall3_flag.txt"
while [ $x -le 1000 ]
do
    unzip third.flag$x.zip $filename
    rm $filename
    filename=chall3_$x.zip 
    x=$(( $x + 1 ))
done
