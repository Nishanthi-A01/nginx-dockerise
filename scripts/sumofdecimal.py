def digit_sum_from_letters(x):
    a = int("%s" % x)
    b = int("%s%s" % (x,x))
    c = int("%s%s%s" % (x,x,x))
    d = int("%s%s%s%s" % (x,x,x,x))
    return a+b+c+d
    print(a+b+c+d)
if __name__ == "__main__":
   decimalnum = input(print"Enter the decimal number:")
   digit_sum_from_letters(decimalnum)

