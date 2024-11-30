#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):
    total = target
    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    x = []
    x.append(num1)
    x.append(num2)

    while count <= target:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        x.append(next_number)
print(x)


target = 100 
x = fibonacciseq(target)
#length = len(list)

def sumEven(x,target):
 
    # Counting frequency of every 
    # element using Counter
     
    # initializing sum 0
    sum = 0
     
    # Traverse the freq and print all
    # sum all elements with even frequency 
    # multiplied by its frequency
    for i in range(0,target):
        if x[i] % 2 == 0:
            sum = sum + x[i]
    print(sum)
 
 
sum = sumEven(x,target)
print(sum)
