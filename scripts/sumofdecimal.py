def sum_n(x, n):
    s = 0
    for i in range(1,n+1):
        s += int(('%d'*i) % tuple([x]*i))
    return s


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   n = input("Enter the number of iterations:")
   total=sum_n(decimalnum,n)
   print(total)


