#!/bin/sh

echo Testing the grep command:

grep "nginx-deployment" ./input.txt

grep -B 4 "volume" ./input.txt

grep -l -i sum *.py
grep -L -i sum *.py

echo Testing sed command with the input file:


sed -e' s/docker /dockerhub/g' input.txt > inputmodified.txt

sed '4 i #This is the extra line' ./input.txt
sed '5 a #This is the extra line' ./input.txt

echo Testing awk commnd with the input file:

awk '($2 == "Reason") {print}' ./input.txt




