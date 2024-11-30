def digit_sum(x):
    lst = [str(x)*i for i in range(1,4)]
    print '+'.join(lst)
    return sum(map(int, lst))
    print(sum(map(int, lst)))


if __name__ == "__main__":
   decimalnum = input("Enter the decimal number:")
   digit_sum(decimalnum)


