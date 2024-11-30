# This script calculates the sum of 100 even fibonacci numbers 


def evenFibSum(limit) :
    
    
 
    # Initialize first two even Fibonacci numbers
    # and their sum
    ef1 = 0
    ef2 = 2
    sm= ef1 + ef2
    i=2 #initialize the fibonacci number counting 
     
    # calculating sum of even Fibonacci value
    while (i <= limit ) :
 
        # get next even value of Fibonacci 
        # sequence
        ef3 = 4 * ef2 + ef1
 
        
 
        # Move to next even number and update
        # sum
        ef1 = ef2
        ef2 = ef3
        i= i+1
        sm = sm + ef2
     
    return sm
 
limit=100
print(evenFibSum(limit))