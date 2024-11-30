#This script calculates the even fibonacci number out of first 100 fibonacci sequence 

def fibonacciseq(target):

    # determine the number of finonacci sequence 
    num1 = 0  # declaring the first two fibonacci number 
    num2 = 1
    next_number = num2  
    count = 1
    list = []
    list.append(num1,num2)

    while count <= target:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        list.append(next_number)
        print(" the list of first ${target} fibonacci dequence: ${list}")       
    return list 



sum([i for i in fibonacciseq(100) if i%2 ==0])