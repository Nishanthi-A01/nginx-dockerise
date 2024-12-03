from decimal import Decimal
def sum_n(x, n):
    s = 0
    for i in range(1,n+1):
        s += Decimal(('%d'*i) % tuple([x]*i))
    return(Decimal(s))


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   iterations = input("Enter the number of iterations:")
   print(type(decimalnum))
   if decimalnum.isdecimal():
      print("The number entered is valid!")
      total=sum_n(Decimal(decimalnum),int(iterations))
      print(total)
   else:
      print("The entered number is invalid")
   


