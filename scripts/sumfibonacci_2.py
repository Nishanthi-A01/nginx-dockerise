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




def sumEven(y,target):
 
    # Counting frequency of every 
    # element using Counter
     
    # initializing sum 0
    sum = 0
     
    # Traverse the freq and print all
    # sum all elements with even frequency 
    # multiplied by its frequency
    for i in range(0,target):
        if y[i]%2 == 0:
            sum = sum + y[i]
    print(sum)
 
 


if __name__ == "__main__":
    target = 100 
    y = fibonacciseq(target)
    sum = sumEven(y,target)
    print(sum)
   
   
