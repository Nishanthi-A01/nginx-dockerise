def digit_sum_from_letters(x):
    a = Decimal("%s" % x)
    b = Decimal("%s%s" % (x,x))
    c = Decimal("%s%s%s" % (x,x,x))
    d = Decimal("%s%s%s%s" % (x,x,x,x))
    sum = a+b+c+d
    print(sum)


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   digit_sum_from_letters(decimalnum)

