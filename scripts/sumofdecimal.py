import decimal

def sum_n(x, n):
    s = 0
    for i in range(1,n+1):
        s += decimal.Decimal(('%d'*i) % tuple([x]*i))
    return(decimal.Decimal(s))


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   iterations = input("Enter the number of iterations:")
   d = decimal.Decimal(decimalnum)
   e = abs(d.as_tuple().exponent) 
   if decimalnum.isdigit() or e >= 0:          
        print("The number entered is valid!")
        total=sum_n(decimal.Decimal(decimalnum),int(iterations))
        print('The result of the sum of decimal value:',total)
   else:
        print("The entered number is invalid")


