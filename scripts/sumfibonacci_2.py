#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):
    total = target
    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    list = [0,1]

    while count <= target:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        list.append(next_number)
        
#print("The list of fibonacci sequence:")  

print(list)

target = 100 
fibonacciseq(target)
     



"""
def sumEven(arr,n):
 
    # Counting frequency of every 
    # element using Counter
    freq = Counter(arr)
     
    # initializing sum 0
    sum = 0
     
    # Traverse the freq and print all
    # sum all elements with even frequency 
    # multiplied by its frequency
    for it in freq:
        if freq[it] % 2 == 0:
            sum = sum + freq[it]
    print(sum)
 
 
# Driver code
n = len(list)
 
sumEven(list, n)
"""
