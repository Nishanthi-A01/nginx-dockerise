#!/bin/sh

#echo &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
echo Testing the grep command:
#echo &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

echo greping nginx-deployment in input.txt file 
grep "nginx-deployment" ./input.txt

echo greping 4 lines before the search item volume  in input.txt file
grep -B 4 "volume" ./input.txt
echo greping file with name sum and .py extension  
grep -l -i sum *.py
echo greping file without name sum and .py extension 
grep -L -i sum *.py

#echo &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
echo Testing sed command with the input file:
#echo &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


echo replacing docker with dockerhub using sed 
sed -e' s/docker/dockerhub/g' input.txt > inputmodified.txt

echo Adding text before the line 4 

sed '4 i #This is the extra line' input.txt
echo adding text after the line 4 
sed '5 a #This is the extra line' input.txt

echo Testing awk commnd with the input file 

awk '($2 == "Reason") {print}' ./input.txt




