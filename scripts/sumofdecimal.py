def digit_sum_from_letters(x):
    a = int("%s" % x)
    b = int("%s%s" % (x,x))
    c = int("%s%s%s" % (x,x,x))
    d = int("%s%s%s%s" % (x,x,x,x))
    sum = a+b+c+d
    print(sum)


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   digit_sum_from_letters(decimalnum)

