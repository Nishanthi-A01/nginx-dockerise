#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):

    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    list = []
    list = list.insert(num1,num2)

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        list = list.insert(nextnumber)
        print(" the list of first ${target} fibonacci dequence: ${list}")       
    return list 

print(" the list of first ${target} fibonacci dequence:")

target = 100 

sum([i for i in fibonacci(target) if i%2 ==0])