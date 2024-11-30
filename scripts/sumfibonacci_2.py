#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):
    total = target
    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    array = []
    array.append(num1)
    array.append(num2)

    while count <= target:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        array.append(next_number)
        
#print("The list of fibonacci sequence:")  

print(array)


target = 100 
array = fibonacciseq(target)
#length = len(list)

def sumEven(array,target):
 
    # Counting frequency of every 
    # element using Counter
     
    # initializing sum 0
    sum = 0
     
    # Traverse the freq and print all
    # sum all elements with even frequency 
    # multiplied by its frequency
    for i in range(0,target):
        if array[i] % 2 == 0:
            sum = sum + array[i]
    print(sum)
 
 
sum = sumEven(array,target)
print(sum)
