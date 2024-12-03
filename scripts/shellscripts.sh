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

echo replacing the 3th occurence of docker with dockerhub using sed 
sed -e' s/docker/dockerhub/3' input.txt > inputmodified.txt

echo Printing only the replaced line  
sed -e' s/docker/dockerhub/p' input.txt 

echo Deleting the particular line from the file 
sed 5d input.txt

echo Deleting the last line from the file 
sed $d input.txt


echo Testing awk commnd with the input file 

awk '($2 == "Reason") {print}' ./input.txt




