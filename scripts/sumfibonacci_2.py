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

    while count <= target-2:
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        x.append(next_number)
    print(x)
    print(type(x))
    print(x[5])
    print(len(x))
    return x




def sumEven(arr,target):
 
    # Counting frequency of every 
    # element using Counter
     
    # initializing sum 0
    sum = 0
    i=0

    for i in range(target):
        if arr[i] % 2 == 0:
            sum = sum + arr[i]
    #print(sum)
    return sum
 
 
if __name__ == "__main__":
    target = 100 
    arr = fibonacciseq(target)
    print(type(arr))
    sumofevennum = sumEven(arr,target)
    print(sumofevennum)
   
   
