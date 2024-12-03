# nginx-deployment
Dockerfile to run nginx version 1.19 in a container. 
alpine is choosen as a Base image 
# security best practices
Running the container configuration as a different user than root , with user given a root permission (entrypoint.sh)
configuring nginx server with https port configured and ssl certificate uploaded (nginx.conf file)

Security test is done at DOCKER registry using DOCKER Scout


## scripts folder under NGINX-DOCKERISE
This folder has all the automation scripts refered the questionnaire point from (4-8)

# point 4 Text Manipulation Problem [5 pts]
Choose or create a text manipulation problem that involves using awk, sed, tr, and/or grep. Solve the problem, considering efficiency and readability

>> sh shelltextmanipulation.sh   ===>  Replacing the namespace/username/password in the secret-template file with env variable using grep/sed
>> sh shellscripts.sh ===> performing few shell manipulation operation with the input.txt 

# point 5 .Text Manipulation with an Object Orientated Programming Language.
I have added the python script which was created by me for validating license file .
>>python3 textmanipulation.py ==> tetant id : txyz primary or backup adapter : priamry/backup 

# point 6 Sum of Even Fibonacci Numbers [10 pts]
Write a program in an Object Oriented Programming language of your choice to calculate the sum of the first 100 Fibonacci numbers that are even. 
>>python3 sumfibonacci_1.py ==> sum of first 100 even fibonacci  numbers 

>>python3 sumfibonacci_2.py ==> sum of firt even fibonacci number out of 100 fibonacci number 

# point 7. Intersection of Sorted Arrays [10 pts]
Write a function in a Object Orientated Programming language of your choice that takes two sorted arrays of integers as input and returns an array containing numbers common to both arrays without duplicates.
>>python3 intersectionofarray.py

# point 8: Decimal Digit Transformation [10 pts]
Write a function in an Object Orientated Programming language of your choice that, when passed a decimal digit X, calculates and returns the value of X + XX + XXX + XXXX. 

>>python3 sumofdecimal.py



