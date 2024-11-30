def digit_sum_from_letters(x):
    a = Decimal("%d" % x)
    b = Decimal("%d%d" % (x,x))
    c = Decimal("%d%d%d" % (x,x,x))
    d = Decimal("%d%d%d%d" % (x,x,x,x))
    sum = a+b+c+d
    print(sum)


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   digit_sum_from_letters(decimalnum)

