import decimal
def sum_n(x, n):
    s = 0
    for i in range(1,n+1):
        s += decimal.Decimal(('%d'*i) % tuple([x]*i))
    return(decimal.Decimal(s))


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   iterations = input("Enter the number of iterations:")
   d= decimal.Decimal(decimalnum)
   e=abs(d.as_tuple().exponent) 
   if decimalnum.isdigit() and e >= 0:          
        print("The number entered is valid!")
        total=sum_n(decimal.Decimal(decimalnum),int(iterations))
        print(total)
   else:
        print("The entered number is invalid")


    
mylist=["100","23.0","45.650","56.00","500.70000"]

for item in mylist:
    print(item)
    d = decimal.Decimal(item)
    e=abs(d.as_tuple().exponent) 
    if e==0:
         print(f"{item} has no decimal places")
    elif e==1:
            print(f"{item} has 1 decimal place")
    elif e==2:
            print(f"{item} has 2 decimal place")
    elif e==3:
            print(f"{item} has 3 decimal place")
    else:
            print(f"{item} is has many decimal places")


