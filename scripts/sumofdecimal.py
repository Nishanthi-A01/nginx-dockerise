def digit_sum_from_letters(x):
    a = float("%f" % x)
    b = float("%f%f" % (x,x))
    c = float("%f%f%f" % (x,x,x))
    d = float("%f%f%f%f" % (x,x,x,x))
    sum = a+b+c+d
    print(sum)


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   digit_sum_from_letters(decimalnum)

