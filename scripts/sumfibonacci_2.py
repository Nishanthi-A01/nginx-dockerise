#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):
    total = target
    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    list = []
    list = list.append[0,1]

    while count <= target:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        list.append(next_number)
        
#print("The list of fibonacci sequence:")  

print(list)
print(type(list))

target = 100 
list = fibonacciseq(target)
#length = len(list)

def sumEven(list,target):
 
    # Counting frequency of every 
    # element using Counter
     
    # initializing sum 0
    sum = 0
     
    # Traverse the freq and print all
    # sum all elements with even frequency 
    # multiplied by its frequency
    for i in list:
        if list[i] % 2 == 0:
            sum = sum + list[i]
    print(sum)
 
 
sum = sumEven(list,target)
print(sum)
